
SEGUIR GENERANDO UN REGEX PARA FILTRAR LAS SALIDAS DEL XML POR UN KEYWORD, CON UNA FUNCION YIELD

import hashlib
import json
import urllib.request
import xml.etree.ElementTree as ET

def obtener_ultimos_articulos(url_feed, num_articulos):
    response = urllib.request.urlopen(url_feed)
    tree = ET.parse(response)
    root = tree.getroot()
    
    ultimos_articulos = []
    
    for item in root.findall('.//item')[:num_articulos]:
        titulo = item.find('title').text
        url = item.find('link').text
        date = item.find('pubDate').text
        
        keywords_element = item.find('.//media:keywords', {'media': 'http://search.yahoo.com/mrss/'})
        keywords = keywords_element.text if keywords_element is not None else ""


        articulo = {
            'title': titulo,
            'url': url,
            'keywords': keywords,
            'date':date

        }

        ultimos_articulos.append(articulo)

    return ultimos_articulos

def hashificar_cadena(cadena):
    hash_obj = hashlib.sha256(cadena.encode('utf-8'))
    return hash_obj.hexdigest()

#normalizar palabras
#regex matcheo

def get_rss():
    url_feed = "https://www.eldiario.es/rss/"

    num_articulos = 10000

    ultimos_articulos = obtener_ultimos_articulos(url_feed, num_articulos)
    hash_id = {hashificar_cadena(art['url']): art for art in ultimos_articulos}
    cadena_json = json.dumps(hash_id, ensure_ascii=False)
    print(cadena_json)
    
    return cadena_json

