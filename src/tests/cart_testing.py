from src.modules.cart import ShoppingCart
from src.modules.product import Product


def test_cart_creation():
    iphone = Product('iPhone 15', 999.99, 'Phone', 1)
    redmi = Product('Redmi Note 15 Pro', 1499.99, 'Laptop', 1)

    cart = ShoppingCart([iphone, redmi])
    assert cart.get_goods == [iphone, redmi]


test_cart_creation()
