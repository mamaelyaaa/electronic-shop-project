class Order:

    def __init__(self, customer, goods, price):
        self._customer = customer
        self._goods = goods
        self._price = price
        self.get_status = 'In progress'

    def change_status(self, new_status):
        if new_status in ['In progress', 'Processed', 'Delivered', 'Canceled']:
            self._status = new_status
        else:
            raise ValueError('Такого статуса нет')

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
    def get_goods(self):
        return self._goods
