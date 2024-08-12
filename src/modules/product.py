class Product:

    def __init__(self, model: str, price: float, category, check_in_storage: int):
        self._model = model
        self._price = price
        self.get_category = category
        self.check_in_storage = check_in_storage

    def get_info(self):
        return f'Model: {self._model}\nPrice: {self._price}$\nIn stock: {self.check_in_storage}'

    @property
    def get_model(self):
        return self._model

    @property
    def get_price(self):
        return self._price

    @property
    def get_category(self):
        return self._category

    @get_category.setter
    def get_category(self, model: str):
        if model.capitalize() in ['Laptop', 'Phone', 'Headphones']:
            self._category = model
        else:
            raise ValueError('Такой категории товаров нет')

    @property
    def check_in_storage(self):
        return self._check_in_storage

    @check_in_storage.setter
    def check_in_storage(self, check: int):
        if check > 0:
            self._check_in_storage = check
        else:
            raise ValueError('Товара нет в наличии')

