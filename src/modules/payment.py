class Payment:

    def __init__(self, price: float, status):
        self._price = price
        self._status = status

    @property
    def get_status(self):
        return self._status

    @get_status.setter
    def get_status(self, status: str):
        if status.capitalize() in ['Paid', 'In progress']:
            self._status = status
        else:
            raise ValueError('Такого статуса оплаты нет')

    @property
    def get_price(self):
        return self._price
