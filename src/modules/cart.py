from src.modules.product import Product


class ShoppingCart:

    def __init__(self, goods: list[Product]):
        self._goods = goods

    def add_to_cart(self, product: Product):
        self._goods.append(product)

    def del_from_cart(self, product: Product):
        for i in range(len(self._goods)):
            if self._goods[i] == product:
                del self._goods[i]

    def get_price(self) -> float:
        cart_price = 0

        for product in self._goods:
            cart_price += product.get_price

        return cart_price

    @property
    def get_goods(self):
        return self._goods
