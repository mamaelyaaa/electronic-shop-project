from src.modules.order import Order


class Payment:

    def __init__(self, price: float):
        self._price = price
        self._status = 'In progress'

    def make_payment(self, order: Order):
        if self.get_price != order.get_price:
            order.change_status('Canceled')
            raise ValueError('The payment amount does not match the order amount :/')
        else:
            self.get_status = 'Paid'
            order.change_status('Processed')
            print(f'Payment was successful! The order {order.get_status.lower()}')

    @property
    def get_status(self):
        return self._status

    @get_status.setter
    def get_status(self, status: str):
        if status.capitalize() in ['Paid', 'In progress']:
            self._status = status
        else:
            raise ValueError('No such status exists')

    @property
    def get_price(self):
        return self._price
