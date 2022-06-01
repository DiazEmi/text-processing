
import urllib.request
import chardet
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient("mongodb+srv://Ies:<pass>@noticias.vltnv.mongodb.net/pln?retryWrites=true&w=majority")
mydb = client["pln"]
mycol = mydb["news"]

def agregarNoticia(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read() 
    the_encoding = chardet.detect(data)['encoding']
    data = data.decode(the_encoding) 
    
    parsed_html = BeautifulSoup(data,features="lxml")
    
    cuerpo = parsed_html.body.find('div', attrs={'class':'cuerpo-nota'}).text
    dic={'categoria':'tecnologiaa','subcategoria':'economia','cuerpo':cuerpo}
    mycol.insert_one(dic)

noticias = ['https://www.eldiariodecarlospaz.com.ar/mundo/2014/11/27/increible-un-corpino-inteligente-que-medira-el-ritmo-cardiaco-7273.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2016/10/19/cordobeses-trajeron-una-vision-de-trabajo-de-silicon-valley-30911.html',
            'https://www.eldiariodecarlospaz.com.ar/informes-especiales/2018/4/3/tras-el-escandalo-en-facebook-instagram-limito-el-acceso-los-datos-de-sus-usuarios-50070.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2020/5/27/google-quito-813-aplicaciones-de-play-store-88730.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2020/8/31/gobernadores-celebraron-el-lanzamiento-del-satelite-saocom-1b-96241.html',
            'https://www.eldiariodecarlospaz.com.ar/viral/2020/10/31/cuales-son-las-aplicaciones-que-tienen-mas-informacion-de-sus-usuarios-101028.html',
            'https://www.eldiariodecarlospaz.com.ar/viral/2020/11/2/video-el-auto-que-se-transforma-en-avion-en-tres-minutos-101140.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2020/12/14/cordoba-fabrica-pulseras-inteligentes-para-la-deteccion-de-covid-19-104434.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2021/8/3/un-club-argentino-lanzo-su-moneda-digital-121735.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2021/8/28/semana-tic-2021-en-toda-cordoba-se-hablara-de-tecnologia-123698.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2021/9/20/schiaretti-cordoba-es-el-principal-polo-de-alta-tecnologia-de-la-argentina-125437.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2021/12/8/logran-un-gran-avance-en-el-uso-de-adn-para-almacenar-informacion-133320.html',
            'https://www.eldiariodecarlospaz.com.ar/viral/tech/2021/12/17/wireframe-online-ventajas-maneras-de-hacerlo-digitalmente-134007.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2021/12/26/premiaron-argentinos-por-la-nave-mas-pequena-economica-de-la-historia-134643.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/3/10/telecom-busca-talento-digital-con-su-programa-level-up-140716.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2022/3/17/la-provincia-impulsa-la-biotecnologia-en-cordoba-141292.html'
            ]


for i in noticias:
    agregarNoticia(i)

espacios = ['',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
            ]

# aca hay una lista con links que yo use para mi base pero si los quieren usar sepan que solo lei el titulo, vi la longitud del texto para que no sea una sola oracion y que corresponda al tema.. no fue muy rigurosa la busqueda

deporteTenis = ['https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/21/taylor-fritz-dio-la-sorpresa-vencio-nadal-en-la-final-de-indian-wells-141519.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/21/djokovic-recupero-el-numero-del-tenis-mundial-141565.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/28/azarenka-anuncio-su-retiro-momentaneo-del-tenis-por-estres-extremo-142119.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/29/cordoba-apuesta-al-crecimiento-del-tenis-adaptado-142179.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/31/francisco-cerundolo-esta-en-semifinales-del-masters-1000-de-miami-142339.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/2/francisco-cerundolo-perdio-en-semis-del-masters-1000-de-miami-142510.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/15/schwartzman-avanzo-cuartos-en-el-masters-1000-de-montecarlo-143480.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/20/tenistas-rusos-bielorrusos-no-podran-jugar-en-wimbledon-143880.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/24/schwartzman-quedo-eliminado-en-el-conde-de-godo-144166.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/25/alcaraz-gano-en-barcelona-ya-es-top-ten-144190.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/26/djokovic-podra-jugar-en-wimbledon-sin-estar-vacunado-144329.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/26/argentina-ya-tiene-rivales-para-las-finales-de-la-copa-davis-144330.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/27/roger-federer-anuncio-cuando-volvera-al-circuito-144369.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/5/2/el-argentino-sebastian-baez-se-consagro-campeon-en-estoril-144692.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/5/3/sebastian-baez-llego-al-puesto-40-del-ranking-mundial-de-tenis-144778.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/5/7/alcaraz-sigue-creciendo-elimino-nadal-en-el-masters-1000-de-madrid-145046.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/5/8/alcaraz-elimino-djokovic-jugara-la-final-del-masters-1000-de-madrid-145112.html'
            ]
deporteBoxeo = ['https://www.eldiariodecarlospaz.com.ar/deportes/2022/1/15/boxeo-el-cordobes-gudino-busca-la-consagracion-ante-yamil-peralta-136267.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/1/18/mike-tyson-cerca-de-pelear-con-el-youtuber-jake-paul-136561.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/1/28/maravilla-martinez-vencio-mcgowan-por-puntos-137348.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/1/28/se-viene-otro-festival-de-box-en-el-estadio-arena-137419.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/1/30/noche-de-box-en-el-arena-137544.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/2/3/brian-castano-peleara-nuevamente-con-jermell-charlo-por-titulos-mundiales-137896.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/2/10/previa-discusion-en-el-aeropuerto-yao-cabrera-se-reunio-con-maidana-en-buenos-aires-138457.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/2/14/chiquito-bracamonte-peleara-en-inglaterra-contra-demsey-mckean-138764.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/2/20/fin-de-semana-con-excelente-ocupacion-turistica-gran-cantidad-de-eventos-139294.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/2/27/el-argentino-fernando-martinez-gano-el-titulo-mundial-de-la-fib-139845.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/1/la-mole-moli-el-paton-basile-pelearian-en-el-luna-park-139953.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/10/se-viene-una-noche-llena-de-adrenalina-en-el-club-sarmiento-140709.html',
            'https://www.eldiariodecarlospaz.com.ar/sucesos/2022/3/10/la-hiena-barrios-seguira-preso-por-violencia-de-genero-140742.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/11/yesica-bopp-defendera-su-titulo-mundial-en-panama-140808.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/13/boxeo-yesica-bopp-perdio-su-titulo-mundial-luego-de-13-anos-140935.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/14/vuelve-lo-mejor-del-boxeo-la-ciudad-141029.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/20/boxeo-en-el-monaco-espace-141483.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/24/peligra-la-pelea-entre-el-chino-maidana-yao-cabrera-141798.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/3/28/falucho-laciar-41-anos-de-consagrarse-campeon-del-mundo-142123.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/8/mayweather-peleara-en-el-helipuerto-de-un-hotel-de-lujo-en-dubai-142954.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/17/el-argentino-carlos-alanis-se-consagro-campeon-mundial-juvenil-de-boxeo-143632.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/23/vuelve-el-boxeo-esta-noche-en-carlos-paz-143970.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/4/24/tyson-fury-se-despidio-del-boxeo-con-un-espectacular-nocaut-144131.html',
            'https://www.eldiariodecarlospaz.com.ar/deportes/2022/5/8/el-ruso-dmitry-bivol-dio-el-batacazo-ante-el-canelo-alvarez-145107.html'
            ]

politicaUcr = ['https://www.eldiariodecarlospaz.com.ar/politica/2021/12/6/ucr-natalia-lenci-reclamo-que-el-radicalismo-vuelva-sus-origenes-133168.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/12/9/la-ucr-de-cordoba-rechaza-la-legalizacion-del-juego-on-line-133422.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/12/17/la-ucr-elige-su-nuevo-presidente-134026.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/12/22/la-ucr-de-carlos-paz-junta-firmas-para-la-ley-de-ficha-limpia-134372.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/12/29/la-ucr-suspendio-arduh-por-impulsar-la-ley-de-juego-online-134892.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/1/9/la-ucr-de-punilla-pide-acciones-urgentes-por-la-crisis-hidrica-135811.htmlhttps://www.eldiariodecarlospaz.com.ar/nacionales/2022/1/17/diputados-radicales-criticaron-la-suspension-de-la-reunion-con-guzman-136493.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/1/24/aseguran-que-aguad-se-ofrecio-como-candidato-vicegobernador-de-juez-137047.htmlhttps://www.eldiariodecarlospaz.com.ar/politica/2022/1/27/arduh-sera-juzgado-por-el-tribunal-de-conducta-de-la-ucr-de-cordoba-137288.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2022/2/1/negriel-gobernador-esta-en-el-operativo-distancia-del-gobierno-nacional-lo-sobreactua-137751.html',
            'https://www.eldiariodecarlospaz.com.ar/sucesos/2022/2/14/la-despedida-de-todo-el-arco-politico-el-gato-romero-138737.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/2/19/carasso-jxc-va-ser-gobierno-en-el-2023-con-el-radicalismo-139216.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2022/3/15/rio-cuarto-juntos-ucr-pide-que-haya-atencion-presencial-en-las-oficinas-de-rentas-141096.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/3/21/bloque-juntos-ucr-se-reunio-con-diputados-nacionales-141592.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/4/18/el-radicalismo-cordobes-debatira-su-futuro-en-villa-giardino-143701.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/4/22/en-villa-giardino-la-ucr-de-cordoba-abrio-el-debate-de-cara-al-2023-144062.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/4/23/el-radicalismo-de-cordoba-propondra-candidatos-de-juntos-por-el-cambio-144110.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/25/la-ucr-definio-en-villa-giardino-las-lineas-seguir-de-cara-al-2023-144188.html'
            ]

politicaPeronista = ['https://www.eldiariodecarlospaz.com.ar/sociedad/2021/5/7/el-legado-de-eva-peron-102-anos-de-su-nacimiento-115130.html',
            'https://www.eldiariodecarlospaz.com.ar/nacionales/2021/7/1/la-camara-de-diputados-rindio-homenaje-peron-47-anos-de-su-muerte-119285.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/7/24/nataliade-la-sota-alejandra-vigo-encabezan-hacemos-por-cordoba-121017.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2021/7/30/escandalo-los-palmeras-denunciaron-guillermo-moreno-121466.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2021/9/16/la-carta-que-escribio-cristina-ante-la-crisis-del-gobierno-125146.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/10/12/el-legislador-walter-saieg-abandono-el-kirchnerismo-127042.html',
            'https://www.eldiariodecarlospaz.com.ar/nacionales/2021/10/15/alberto-fernandez-llamo-movilizarse-en-las-plazas-por-el-17-de-octubre-127266.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/10/15/dia-de-la-lealtad-pusieron-en-valor-la-plazoleta-de-peron-evita-127312.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/10/16/cristina-fernandez-el-peronismo-esta-mas-vigente-que-nunca-127374.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2021/10/18/militancia-organizaciones-sociales-llenaron-la-plaza-de-mayo-por-el-dia-de-la-lealtad-127443.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/2/5/los-105-anos-fallecio-ana-macri-fundadora-partido-peronista-femenino-138033.html',
            'https://www.eldiariodecarlospaz.com.ar/mundo/2022/2/7/alberto-fernandez-xi-jinping-si-fuera-argentino-seria-peronista-138169.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/2/28/schiaretti-presidira-el-partido-justicialista-partir-del-27-de-marzo-139944.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/3/1/llaryora-condeno-los-ataques-de-rusia-ucrania-139990.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/3/2/pj-schiaretti-logro-la-unidad-nivel-provincial-pero-en-punilla-habra-internas-140031.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/3/21/entra-en-la-recta-final-la-interna-peronista-de-punilla-141494.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/3/24/con-el-apoyo-de-las-62-organizaciones-se-derrumbara-una-dinastia-141850.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2022/3/27/se-conocen-los-primeros-datos-de-la-interna-peronista-en-punilla-142051.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/1/murio-juan-jose-goenaga-querido-vecino-empresario-hotelero-142472.html',
            'https://www.eldiariodecarlospaz.com.ar/sucesos/2022/4/8/el-exgobernador-de-entre-rios-sergio-urribarri-fue-condenado-anos-de-prision-142961.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/5/7/homenajes-eva-peron-103-anos-de-su-nacimiento-145089.html',
            'https://www.eldiariodecarlospaz.com.ar/informes-especiales/2022/5/7/nacimiento-de-evita-145091.html'
            ]

politicaMilei = ['https://www.eldiariodecarlospaz.com.ar/espectaculos/2018/8/7/javier-milei-oficializo-novia-con-un-super-beso-55374.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2019/3/19/marcela-tinayre-echo-de-su-programa-javier-milei-luego-de-que-hiciese-llorar-sol-perez-65361.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2020/9/27/javier-milei-anuncio-que-sera-candidato-diputado-98381.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2020/12/10/un-grupo-de-radicales-formo-el-partido-libertario-quien-se-sumara-en-punilla-104174.html',
            'https://www.eldiariodecarlospaz.com.ar/politica/2021/2/13/espert-milei-recorren-este-sabado-la-costanera-de-carlos-paz-108947.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/1/6/javier-milei-anuncio-que-sorteara-su-sueldo-de-diputado-como-participar-135503.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/1/10/hay-una-pagina-trucha-del-sorteo-de-milei-135882.html',
            'https://www.eldiariodecarlospaz.com.ar/nacionales/2022/1/13/javier-milei-sorteo-su-primer-sueldo-de-diputado-nacional-136097.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/1/17/javier-milei-tiene-coronavirus-136494.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/2/2/javier-milei-volvera-sortear-su-sueldo-como-participar-137840.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/2/10/javier-milei-volvio-sortear-su-sueldo-de-diputado-138506.html'
            ]

espectaculoCine = ['https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/1/13/la-ultima-entrega-de-hotel-transylvania-en-amazon-prime-video-136092.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/1/14/obra-maestra-el-padrino-volvera-los-cines-en-hd-136180.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/1/25/cine-en-los-barrios-cronograma-de-esta-semana-137069.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/2/4/festival-de-cine-japones-podra-verse-gratis-online-137939.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/2/8/graham-king-hara-un-film-sobre-la-vida-de-michael-jackson-138294.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/2/10/filmaran-una-biopic-sobre-franz-kafka-138422.html',
            'https://www.eldiariodecarlospaz.com.ar/turismo/2022/2/11/jesus-maria-se-viene-el-ciclo-de-cine-bajo-las-estrellas-138582.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/2/14/aparecio-el-primer-teaser-de-el-senor-de-los-anillos-los-anillos-de-poder-138784.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/2/18/presentaron-elvis-la-biopic-del-rey-del-rock-139111.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/2/llega-los-cines-el-nuevo-batman-con-robert-pattinson-140022.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/14/llega-los-cines-animales-fantasticos-los-secretos-de-dumbledore-143403.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/15/esta-noche-sigue-el-cine-en-la-plaza-prospero-molina-143532.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/5/5/presentaron-el-festival-internacional-de-cine-independiente-de-cosquin-144964.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/14/llega-los-cines-animales-fantasticos-los-secretos-de-dumbledore-143403.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/19/el-film-argentino-herbaria-fue-premiado-en-suiza-143741.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/19/el-gerente-sera-la-primera-pelicula-argentina-en-paramount-143739.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/22/los-85-de-jack-nicholson-el-genio-seductor-de-hollywood-144028.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/25/una-pelicula-cordobesa-fue-premiada-en-uruguay-144226.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/26/sublime-del-argentino-biasin-gano-como-mejor-filme-iberoamericano-en-seattle-144274.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/26/el-festival-internacional-de-cine-independiente-anuncio-su-programacion-144298.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/5/2/el-filme-argentino-karnawal-mejor-opera-prima-de-los-ix-premios-platino-144697.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/5/5/scorsese-narrara-producira-un-documental-sobre-the-archers-144918.html'
            ]

espectaculoMusica = ['https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/17/jairo-sera-el-plato-fuerte-de-la-fiesta-aniversario-de-tanti-141269.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/18/keith-richards-relanza-main-offender-el-album-que-sello-su-relacion-con-argentina-141365.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/18/tini-postergo-su-presentacion-en-cordoba-141382.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/21/foo-fighters-cerro-el-lollapalooza-puro-rock-141568.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/24/keith-richards-le-envio-un-mensaje-sus-fans-argentinos-141797.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/25/marina-gonzalez-una-de-las-voces-mas-poderosas-de-punilla-141918.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/3/26/murio-taylor-hawkins-el-baterista-de-foo-fighters-141954.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/26/a-ha-dio-un-gran-show-en-buenos-aires-recreo-sus-clasicos-141966.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/27/l-gante-se-tiro-del-escenario-142028.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/31/maria-becerra-hara-historia-en-los-grammy-junto-balvin-142337.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/31/el-duo-malavista-se-presenta-en-santo-diablo-142357.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/4/no-te-va-gustar-tocara-en-rio-cuarto-cordoba-142637.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/6/se-agotaron-las-entradas-para-ver-lali-esposito-en-el-luna-park-142805.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/12/ruben-rada-tocara-en-cordoba-el-12-de-mayo-143235.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/13/regresa-la-musica-cuyana-cosquin-143297.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/13/wos-presentara-oscuro-extasis-en-la-plaza-de-la-musica-143375.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/19/rosalia-volvera-argentina-en-agosto-143742.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/19/comienza-la-venta-de-entradas-para-el-show-de-daddy-yankee-en-argentina-143743.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/22/kiss-llega-argentina-en-su-gira-de-despedida-143991.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/24/kiss-se-despidio-de-argentina-con-un-show-espectacular-144165.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/29/joan-manuel-serrat-inicio-en-nueva-york-su-gira-de-despedida-144544.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/5/1/metallica-brillo-ante-una-multitud-en-su-regreso-argentina-144673.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/5/1/la-mona-dara-un-show-gratuito-en-el-obelisco-144677.html'
            ]

espectaculoSeries = ['https://www.eldiariodecarlospaz.com.ar/espectaculos/2020/9/19/la-serie-sobre-la-banda-menudo-llega-amazon-prime-video-97719.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2021/1/27/better-call-saul-the-crown-poco-ortodoxa-series-ganadoras-en-los-afi-2020-107644.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2021/2/26/mentes-criminales-se-convirtio-en-la-serie-mas-vista-del-streaming-109874.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2021/8/3/ya-tiene-fecha-la-serie-de-el-senor-de-los-anillos-121742.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2021/8/27/la-serie-de-maradona-se-estrenara-fines-de-octubre-123611.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2021/9/1/lali-esposito-protagoniza-produce-la-serie-el-fin-del-amor-123965.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2021/10/29/se-estrenara-hoy-maradona-sueno-bendito-129296.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/2/13/las-series-estreno-de-netflix-que-no-te-podes-perder-138664.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/2/19/filman-una-serie-sobre-fito-paez-que-se-vera-en-netflix-139168.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/2/24/la-secuela-de-vikingos-valhalla-llega-netflix-139578.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/7/una-actriz-de-la-casa-de-papel-filmara-una-pelicula-en-argentina-140400.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/10/la-segunda-entrega-de-bridgerton-llegara-el-25-de-marzo-140681.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/17/sandra-bullock-se-retirara-de-la-actuacion-por-un-tiempo-141225.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/12/un-nuevo-documental-sobre-marilyn-llega-netflix-143291.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/19/regresan-los-simuladores-despues-de-veinte-anos-141388.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/3/31/moon-knight-un-nuevo-superheroe-llega-disney-142330.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/17/privilegios-del-poder-violencia-de-genero-en-anatomia-de-un-escandalo-143602.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/4/20/llega-netflix-la-segunda-temporada-de-muneca-rusa-143833.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/5/2/robert-de-niro-comenzo-filmar-en-argentina-144744.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/5/6/star-anuncio-el-inicio-de-la-produccion-de-la-serie-argentina-con-robert-de-niro-144977.html',
            'https://www.eldiariodecarlospaz.com.ar/espectaculos/2022/5/8/las-tres-series-policiales-que-llegan-la-tv-145142.html'
            ]

economia = ['https://www.eldiariodecarlospaz.com.ar/nacionales/2022/3/23/fernandez-georgieva-destacaron-la-importancia-del-acuerdo-con-el-fmi-141713.html',
            'https://www.eldiariodecarlospaz.com.ar/nacionales/2022/3/31/por-la-inflacion-se-pagara-un-bono-los-jubilados-que-cobran-menos-142353.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/3/31/feletti-admitio-que-la-inflacion-de-marzo-va-ser-alta-142390.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/3/31/fernandez-buscamos-que-la-inflacion-no-coma-los-salarios-142399.html',
            'https://www.eldiariodecarlospaz.com.ar/mundo/2022/4/1/para-el-fmi-el-acuerdo-con-argentina-establece-objetivos-pragmaticos-realistas-142426.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/2/la-recaudacion-tributaria-aumento-625-en-marzo-142533.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/8/veteranos-de-malvinas-tendran-acceso-los-prestamos-de-anses-142996.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/8/los-plazos-fijos-uva-ganarian-la-inflacion-con-una-tasa-del-5655-143036.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/12/guzman-anticipo-que-superara-el-6-la-inflacion-de-marzo-143251.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2022/4/14/la-economia-del-conocimiento-de-cordoba-ya-cuenta-con-50-empresas-143471.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/18/el-gobierno-anunciara-medidas-para-mejorar-salarios-ante-la-inflacion-143712.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/18/fernandez-guzman-anunciaron-un-bono-para-monotributistas-jubilados-143723.html',
            'https://www.eldiariodecarlospaz.com.ar/nacionales/2022/4/19/en-que-consiste-el-impuesto-la-renta-extraordinaria-143749.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/20/el-fmi-elevo-las-proyecciones-de-crecimiento-de-la-argentina-4-en-2022-143837.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/20/llaryora-viajo-san-juan-para-continuar-impulsando-la-economia-circular-en-el-pais-143852.html',
            'https://www.eldiariodecarlospaz.com.ar/nacionales/2022/4/21/guzman-aseguro-que-el-problema-inflacionario-se-incremento-con-la-guerra-143942.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/23/guzman-se-reunio-con-georgieva-para-revisar-el-acuerdo-con-el-fmi-144104.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/24/fernandez-no-somos-un-gobierno-que-ajusta-somos-un-gobierno-que-invierte-144152.html',
            'https://www.eldiariodecarlospaz.com.ar/nacionales/2022/3/19/el-presidente-lanzo-un-paquete-de-medidas-contra-la-inflacion-141403.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/26/anses-como-acceder-al-bono-de-18000-cuales-son-los-requisitos-144180.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/4/28/invertir-en-acciones-una-forma-de-ahorro-que-continua-siendo-interesante-144456.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2022/4/30/economia-popular-se-entregaron-maquinarias-herramientas-emprendedores-144629.html',
            'https://www.eldiariodecarlospaz.com.ar/provincial/2022/5/3/la-provincia-adelanta-mayo-el-incremento-salarial-del-10-estatales-144824.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/5/3/cosquin-busca-sanear-una-deuda-millonaria-con-epec-de-otras-gestiones-144826.html',
            'https://www.eldiariodecarlospaz.com.ar/sociedad/2022/5/5/se-homologo-el-aumento-empleados-de-comercio-144910.html'
            ]


categoria = [
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia',
            'https://www.eldiariodecarlospaz.com.ar/noticia'
            ]