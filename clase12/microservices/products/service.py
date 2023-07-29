from nameko.events import EventDispatcher
from nameko.rpc import rpc

from products.exceptions import NotFound
from products.storage import Storage
from products.schemas import ProductSchema

import random

class productsService:
    name = 'products'

    db = Storage()
    event_dispatcher = EventDispatcher()

    @rpc
    def get(self, product_id):
        product = self.db.get_product(product_id)

        if not product:
            raise NotFound('product with id {} not found'.format(product_id))

        return ProductSchema().dump(product)

    @rpc
    def create(self, product):
        self.db.store_product(product)

        product = ProductSchema().dump(product)

        self.event_dispatcher('product_created', {
            'product': product,
        })

        return product