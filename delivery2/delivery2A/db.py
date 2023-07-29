from dataclasses import dataclass
from decimal import Decimal
from pymongo import MongoClient


@dataclass
class Article:
    nombre: str
    precio: float
    cantidad: int
    descripcion: str
    tipo: str

    def __str__(self):
        return f"Object {self.nombre}|{self.precio}|{self.antidad}|{self.descripcion}"
    
    #TODO def __postinit__(self): Checkear si el HASH EXISTE? y si ya se ha accedido al enlace?


class MongoDBInterface:
    """
    Clase de interfaz con mi colección y BD
    """
    def __init__(self, database_name: str, collection_name: str):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

        print(self.client.server_info())

    def insert_product(self, product):
        return self.collection.insert_one(product.__dict__).inserted_id

    def close_connection(self):
        self.client.close()
    
    def drop_collection(self):
        self.collection.drop()
        
interactor = MongoDBInterface('tienda', 'productos')