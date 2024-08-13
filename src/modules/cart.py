from src.modules.product import Product


class ShoppingCart:

    def __init__(self):
        self._goods: list[Product] = []

    def add_to_cart(self, *products) -> None:
        self._goods += [*products]

    def del_from_cart(self, product: Product) -> None:
        self._goods.pop(self._goods.index(product))

    def get_price(self) -> float:
        return sum(i.get_price for i in self._goods)

    @property
    def get_goods(self):
        return self._goods
