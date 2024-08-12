from src.modules.customer import Customer


def test_customer_creation():
    customer = Customer('Vladimir', 'Popov', 'vova@gmail.com', '+88005553535')

    assert customer.get_name == 'Vladimir'
    assert customer.get_surname == 'Popov'
    assert customer.get_email == 'vova@gmail.com'
    assert len(customer.get_phone) == 12
    assert customer.get_cart is None


test_customer_creation()
