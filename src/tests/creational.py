from src.modules.product import Product
from src.modules.cart import ShoppingCart
from src.modules.customer import Customer
from src.modules.order import Order
from src.modules.payment import Payment


def test_product_creation():
    product = Product('Redmi Note 15 Pro', 1499.99, 'Laptop', 2)
    assert product.get_model == 'Redmi Note 15 Pro'
    assert product.get_price == 1499.99
    assert product.get_category == 'Laptop'
    assert product.check_in_storage == 2


def test_cart_creation():
    iphone = Product('iPhone 15', 999.99, 'Phone', 1)
    redmi = Product('Redmi Note 15 Pro', 1499.99, 'Laptop', 1)

    cart = ShoppingCart()
    cart.add_to_cart(iphone)
    cart.add_to_cart(redmi)
    assert cart.get_goods == [iphone, redmi]
    cart.del_from_cart(redmi)
    assert cart.get_goods == [iphone]


def test_customer_creation():
    customer = Customer('Vladimir', 'Popov', 'vova@gmail.com', '+88005553535')

    assert customer.get_name == 'Vladimir'
    assert customer.get_surname == 'Popov'
    assert customer.get_email == 'vova@gmail.com'
    assert len(customer.get_phone) == 12
    assert customer.get_cart is None


def test_order_creation():
    iphone = Product('iPhone 15', 999.99, 'Phone', 1)
    redmi = Product('Redmi Note 15 Pro', 1499.99, 'Laptop', 1)
    cart = ShoppingCart()

    customer = Customer('Vladimir', 'Popov', 'vova@gmail.com', '+88005553535', cart)
    order = Order(1, 'In progress')

    assert order.get_order_id == 1
    assert order.get_status == 'In progress'


def test_payment_creation():
    payment = Payment(2000.99, 'Paid')

    assert payment.get_price == 2000.99
    assert payment.get_status == 'Paid'


test_product_creation()
test_cart_creation()
test_customer_creation()
test_order_creation()
test_payment_creation()
