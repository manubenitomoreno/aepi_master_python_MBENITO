import json

from orders.exceptions import NotFound


class Storage:
    
    @classmethod
    def read_orders(cls) -> dict:
        try:
            with open("orders.json") as handler:
                return json.loads(handler.read())
        except Exception as exc:
            print(exc)
            return {}

    @classmethod
    def store_order(cls, order):
        orders = cls.read_orders()
        orders.update({
            order["id"]: order
        })
        cls.save_orders(orders)

    @classmethod
    def get_order(cls, order_id):
        try:
            orders = cls.read_orders()
            order = orders[str(order_id)]
        except Exception as exc:
            raise NotFound()
        return order

    @classmethod
    def save_orders(cls, orders):
        with open("orders.json", "w") as storage:
            print(json.dumps(orders),file=storage)

