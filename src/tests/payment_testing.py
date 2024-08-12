from src.modules.customer import Customer
from src.modules.payment import Payment


def test_payment_creation():
    payment = Payment(2000.99, 'Paid')

    assert payment.get_price == 2000.99
    assert payment.get_status == 'Paid'


test_payment_creation()
