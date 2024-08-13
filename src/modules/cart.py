from src.modules.product import Product


class ShoppingCart:

    def __init__(self):
        self.__goods: list[Product] = []

    def add_to_cart(self, *products) -> None:
        self.__goods += [*products]

    def del_from_cart(self, product: Product) -> None:
        self.__goods.pop(self.__goods.index(product))

    def get_price(self) -> float:
        return sum(i.get_price for i in self.__goods)

    @property
    def get_goods(self):
        return self.__goods
