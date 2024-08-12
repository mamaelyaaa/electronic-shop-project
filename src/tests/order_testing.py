from src.modules.cart import ShoppingCart
from src.modules.customer import Customer
from src.modules.order import Order
from src.modules.product import Product


def test_order_creation():
    iphone = Product('iPhone 15', 999.99, 'Phone', 1)
    redmi = Product('Redmi Note 15 Pro', 1499.99, 'Laptop', 1)
    cart = ShoppingCart([iphone, redmi])

    customer = Customer('Vladimir', 'Popov', 'vova@gmail.com', '+88005553535', cart)
    order = Order(1, customer, 'In progress')

    assert order.get_order_id == 1
    assert order.get_status == 'In progress'
    assert order.get_goods == [iphone, redmi]


test_order_creation()
