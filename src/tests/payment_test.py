from src.modules.cart import ShoppingCart
from src.modules.customer import Customer
from src.modules.payment import Payment
from src.modules.product import Product, Phone


def test_payment_status():
    customer = Customer("Иван Иванов", "ivan@example.com", "+12345678901")
    product1 = Phone("iPhone 14", 999.99, 50)
    product2 = Product("AirPods", 199.99, "Wireless earphones", 100)

    cart = ShoppingCart()
    cart.add_to_cart(product1, product2)

    order = customer.place_an_order(cart)

    payment = Payment(order.get_price)
    assert payment.get_status == 'In progress'
    payment.make_payment(order)
    assert order.get_status == 'Processed'


test_payment_status()
