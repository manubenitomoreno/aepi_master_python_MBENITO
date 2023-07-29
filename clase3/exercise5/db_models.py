from pymongo import MongoClient
from dataclasses import dataclass
from decimal import Decimal
import random
import string

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int
    descripcion: str
    tipo: str

    def __str__(self):
        return f"Object {self.nombre}|{self.precio}|{self.cantidad}|{self.descripcion}"

class MongoDBInterface:
    def __init__(self, database_name: str, collection_name: str):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
        #print(self.client.server_info())

    def insert_product(self, product):
        return self.collection.insert_one(product.__dict__).inserted_id

    def close_connection(self):
        self.client.close()
    
    def drop_collection(self):
        self.collection.drop()

    def populate_random_collection(self, num_products: int):
        tipos = [f'tipo_{n}' for n in range(0, 5)]

        def generate_random_string(length: int) -> str:
            letters = string.ascii_letters
            return ''.join(random.choice(letters) for _ in range(length))

        for _ in range(num_products):
            nombre = generate_random_string(10)
            precio = round(random.uniform(10, 1000), 2)
            cantidad = random.randint(1, 100)
            descripcion = generate_random_string(50)
            tipo = random.choice(tipos)

            product = Producto(nombre, precio, cantidad, descripcion, tipo)
            self.insert_product(product)

        print(f"Successfully populated {num_products} random products in the collection.")
