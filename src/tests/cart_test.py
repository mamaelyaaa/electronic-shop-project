from src.modules.cart import ShoppingCart
from src.modules.product import Product


def test_cart_updating():
    iphone = Product('iPhone 15', 999.99, 'Phone', 1)
    redmi1 = Product('Redmi Note 15 Pro', 1499.99, 'Laptop', 1)
    redmi2 = Product('Redmi Note 14', 1299.99, 'Laptop', 3)
    cart = ShoppingCart()

    cart.add_to_cart(iphone, redmi1)
    cart.add_to_cart(redmi2)

    assert cart.get_goods == [iphone, redmi1, redmi2]
    assert cart.get_price() == iphone.get_price + redmi1.get_price + redmi2.get_price

    cart.del_from_cart(redmi1)
    assert cart.get_goods == [iphone, redmi2]


test_cart_updating()
