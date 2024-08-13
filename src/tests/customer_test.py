from src.modules.cart import ShoppingCart
from src.modules.customer import Customer
from src.modules.product import Product


def test_customer_order_connection():
    customer = Customer('Vladimir Popov', 'vova@gmail.com', '+88005553535')
    cart = ShoppingCart()
    product1 = Product('Redmi Note 15 Pro', 1499.99, 'Laptop', 1)
    product2 = Product('Samsung A99', 899.99, 'Phone', 5)
    product3 = Product('DT 990 PRO', 1099.99, 'Headphones', 2)

    cart.add_to_cart(product1, product2, product3)

    order = customer.place_an_order(cart)
    assert order.get_status == 'In progress'
    order.change_status('Delivered')
    assert order.get_status == 'Delivered'


test_customer_order_connection()
