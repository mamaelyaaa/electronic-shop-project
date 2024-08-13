from src.modules.cart import ShoppingCart
from src.modules.customer import Customer
from src.modules.product import Product


def test_cart_update():
    samsung = Product('Samsung A99', 899.99, 'Phone', 5)
    beyerdynamic = Product('DT 990 PRO', 1099.99, 'Headphones', 2)

    cart = ShoppingCart()

    cart.add_to_cart(samsung)
    cart.add_to_cart(beyerdynamic)

    assert len(cart.get_goods) == 2

    cart.del_from_cart(samsung)
    assert cart.get_goods == [beyerdynamic]


def test_order_creation():
    customer = Customer('Ivan', 'Ivanov', 'ivan@mail.ru', '+79876543210')
    iphone = Product('iPhone 20', 3000.99, 'phone', 1)
    cart = ShoppingCart()
    cart.add_to_cart(iphone)
    order = customer.place_an_order(cart)

    assert order.get_status == 'In progress'
    assert order.get_order_id == 1
    assert order.get_order_price()


test_cart_update()
