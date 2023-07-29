from nameko.events import EventDispatcher
from nameko.rpc import rpc

from orders.exceptions import NotFound
from orders.storage import Storage
from orders.schemas import OrderSchema

import random

class OrdersService:
    name = 'orders'

    db = Storage()
    event_dispatcher = EventDispatcher()

    @rpc
    def get_order(self, order_id):
        order = self.db.get_order(order_id)

        if not order:
            raise NotFound('Order with id {} not found'.format(order_id))

        return OrderSchema().dump(order)

    @rpc
    def create_order(self, order_details):
        order = dict(
            id=random.randint(1,2000),
            order_details=[
                dict(
                    product_id=order_detail['product_id'],
                    price=order_detail['price'],
                    quantity=order_detail['quantity']
                )
                for order_detail in order_details
            ]
        )
        self.db.store_order(order)

        order = OrderSchema().dump(order)

        self.event_dispatcher('order_created', {
            'order': order,
        })

        return order