import json

from products.exceptions import NotFound


class Storage:
    
    @classmethod
    def read_products(cls) -> dict:
        try:
            with open("products.json") as handler:
                return json.loads(handler.read())
        except Exception as exc:
            print(exc)
            return {}

    @classmethod
    def store_product(cls, product):
        products = cls.read_products()
        products.update({
            product["id"]: product
        })
        cls.save_products(products)

    @classmethod
    def get_product(cls, product_id):
        try:
            products = cls.read_products()
            product = products[str(product_id)]
        except Exception as exc:
            raise NotFound()
        return product

    @classmethod
    def save_products(cls, products):
        with open("products.json", "w") as storage:
            print(json.dumps(products),file=storage)

