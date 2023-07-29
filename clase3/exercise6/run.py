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

        articulo = {
            'title': titulo,
            'url': url
        }

        ultimos_articulos.append(articulo)

    return ultimos_articulos

def hashificar_cadena(cadena):
    hash_obj = hashlib.sha256(cadena.encode('utf-8'))
    return hash_obj.hexdigest()

def main():
    url_feed = 'https://elpais.com/rss/elpais/portada.xml'
    num_articulos = 3

    ultimos_articulos = obtener_ultimos_articulos(url_feed, num_articulos)
    cadena_json = json.dumps({'articles': ultimos_articulos}, ensure_ascii=False)
    cadena_hash = hashificar_cadena(cadena_json)

    print('Cadena JSON:')
    print(cadena_json)
    print('Cadena hash:')
    print(cadena_hash)

if __name__=='__main__':
    main()
