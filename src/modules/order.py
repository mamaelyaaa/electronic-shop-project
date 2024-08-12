from src.modules.customer import Customer


class Order:

    def __init__(self, order_id: int, customer: Customer, status):
        self._order_id = order_id
        self._customer = customer
        self.get_status = status
        self._goods = customer.cart.get_goods

    def change_status(self, new_status):
        self._status = new_status

    @property
    def get_status(self):
        return self._status

    @get_status.setter
    def get_status(self, status):
        if status in ['In progress', 'Processed', 'Delivered', 'Canceled']:
            self._status = status
        else:
            raise ValueError('Такого статуса нет')

    @property
    def get_order_id(self):
        return self._order_id

    @property
    def get_goods(self):
        return self._goods

    def get_order_price(self):
        return self._goods
