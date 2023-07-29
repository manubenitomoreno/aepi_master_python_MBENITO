"""
A. Implementa un lector de feeds RSS de las siguientes características:
    - Los artículos se guardarán en una colección de artículos en MongoDB.
    - La configuración de qué feeds descargar y otras configuraciones que estimes 
      necesarias se almacenarán en un fichero config.json
    - Tendrás una script de python que se encargará de descargar los feeds
      registrados en el config.json y los introducirá en la colección de mongo,
      evitando duplicados gracias a funciones que hemos visto en clase.
      Aprovecha la tecnología de concurrencia que estimes necesaria sin olvidar buenas prácticas
      de espera entre peticiones en las descargas.
    - Last but not least, implementa una forma de leer los artículos y marcarlos como
      leídos.
"""

#Crear DB en Mongo, y una coleccion
#fichero config para la rss
#cuando corra, descarga los feeds necesarios y a la coleccion

from rss import get_rss
if __name__ == "__main__":
    get_rss()
