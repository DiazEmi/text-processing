
import pymongo

client = pymongo.MongoClient("mongodb+srv://Ies:yolo@noticias.vltnv.mongodb.net/pln?retryWrites=true&w=majority")
mydb = client["pln"]
mycol = mydb["news"]
item_details = mycol.find()
list_categoria=[]
list_cuerpo=[]

for item in item_details:
    list_categoria.append(item['categoria'])
    list_cuerpo.append(item['cuerpo'])



categorias = ['deporte', 'economia', 'politica', 'tecnologia']

def Datos(categoria):
    cuerpo = ''
    for posicion in range(len(list_categoria)):
        if list_categoria[posicion] == categoria:
            cuerpo = cuerpo + list_cuerpo[posicion]
    return cuerpo
    
def preProcesado(cuerpo):
    
    cuerpo = cuerpo.lower()
    caracteres = ['\n' , '(' , ')' , '.' , ',' , ';' , ':' , '"' , '“' , '<' , '>']
    for caracter in caracteres:
        cuerpo = cuerpo.replace(caracter , '')
    
    for i in range(10):
        numero = str(i)
        cuerpo = cuerpo.replace(numero , '')
    
    palabras = cuerpo.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] = diccionario[palabra] + 1
        else:
            diccionario[palabra] = 1
            
    orden = {k: v for k, v in sorted(diccionario.items(), key=lambda item: item[1],reverse = True)}
    
    return orden

def filtrado(diccionario):
    palabrasInutiles = [palabra for palabra in diccionario if diccionario[palabra]<2]
    for palabra in palabrasInutiles:
        del diccionario[palabra]
    return diccionario
        

def StopWords(Economia , Deporte , Tecno , Politica):
    palabrasDeporte = [list(Deporte.keys())[cantidad] for cantidad in range(len(Deporte))]
    palabrasEconomia = [list(Economia.keys())[cantidad] for cantidad in range(len(Economia))]
    palabrasTecno = [list(Tecno.keys())[cantidad] for cantidad in range(len(Tecno))]
    palabrasPolitica = [list(Politica.keys())[cantidad] for cantidad in range(len(Politica))]
    stopWords = [palabra for palabra in palabrasEconomia if (palabra in palabrasDeporte) and (palabra in palabrasTecno) and (palabra in palabrasPolitica)]
    return stopWords

cuerpoDeporte = Datos('deporte')
cuerpoEconomia = Datos('economia')
cuerpoTecno = Datos('tecnologia')
cuerpoPolitica = Datos('politica')


diccDeporte = preProcesado(cuerpoDeporte)
diccEconomia = preProcesado(cuerpoEconomia)
diccTecno = preProcesado(cuerpoTecno)
diccPolitica = preProcesado(cuerpoPolitica)

diccEconomia = filtrado(diccEconomia)
diccDeporte = filtrado(diccDeporte)
diccTecno = filtrado(diccTecno)
diccPolitica = filtrado(diccPolitica)

stopWords = StopWords(diccEconomia,diccDeporte,diccTecno,diccPolitica) 
    
for palabra in stopWords:
 del diccEconomia[palabra]
 del diccDeporte[palabra]
 del diccTecno[palabra]
 del diccPolitica[palabra]

pesosEconomia = {}       
for palabra in diccEconomia:
    contador = 0
    if palabra in diccDeporte:
        contador += (1/3)
    if palabra in diccTecno:
        contador += (1/3)
    if palabra in diccPolitica:
        contador += (1/3)
    pesosEconomia[palabra] = 1 - contador

pesosDeporte = {}       
for palabra in diccDeporte:
    contador = 0
    if palabra in diccEconomia:
        contador += (1/3)
    if palabra in diccTecno:
        contador += (1/3)
    if palabra in diccPolitica:
        contador += (1/3)
    pesosDeporte[palabra] = 1 - contador
    
pesosTecno = {}       
for palabra in diccTecno:
    contador = 0
    if palabra in diccDeporte:
        contador += (1/3)
    if palabra in diccEconomia:
        contador += (1/3)
    if palabra in diccPolitica:
        contador += (1/3)
    pesosTecno[palabra] = 1 - contador

pesosPolitica = {}       
for palabra in diccPolitica:
    contador = 0
    if palabra in diccDeporte:
        contador += (1/3)
    if palabra in diccEconomia:
        contador += (1/3)
    if palabra in diccTecno:
        contador += (1/3)
    pesosPolitica[palabra] = 1 - contador

textoNuevo = 'El costo de los productos que integran la Canasta Básica Alimentaria (CBA) subió 6,7% en abril, lo que determinó que una familia conformada por dos adultos y dos hijos menores necesita percibir ingresos por $ 42.527 para no caer en la indigencia, informó este martes el Instituto Nacional de Estadística y Censos (Indec). En tanto, el costo de la Canasta Básica Total (CBT) marcó un incrementó de 6,2% en abril, con lo que una familia integrada tipo debió contar con ingresos por un monto total estimado en $ 95.260 para no caer debajo de la línea de la pobreza. En marzo pasado, el costo de la canasta básica alimentaria había subido 6,5% hasta un monto de $ 39.862, mientras que la canasta básica total registró un aumento de 7% hasta un monto total de $ 89.690. El Indec informó la semana pasada que el Índice de Precios al Consumidor (IPC) registró en abril un avance de 6%, con una suba de 5,9% en alimentos y bebidas no alcohólicas.'

diccNuevo = preProcesado(textoNuevo)
diccNuevo = filtrado(diccNuevo)
for palabra in stopWords:
    if palabra in diccNuevo:
        del diccNuevo[palabra]
        
diccCategoria = {'deporte':0,'politica':0,'tecnologia':0,'economia':0}
contador = 0
factor = 1/(len(diccNuevo)+1)
for palabra in diccNuevo:
    if palabra in pesosDeporte:
        diccCategoria['deporte'] += ((pesosDeporte[palabra] * diccNuevo[palabra]) * (1-contador))
    if palabra in pesosTecno:
        diccCategoria['tecnologia'] += ((pesosTecno[palabra] * diccNuevo[palabra]) * (1-contador))
    if palabra in pesosPolitica:
        diccCategoria['politica'] += ((pesosPolitica[palabra] * diccNuevo[palabra]) * (1-contador))
    if palabra in pesosEconomia:
        diccCategoria['economia'] += ((pesosEconomia[palabra] * diccNuevo[palabra]) * (1-contador))
    contador += factor
    

CategoriaElegida = max(diccCategoria, key=diccCategoria.get)

print(CategoriaElegida)































































