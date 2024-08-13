from src.modules.product import Product


def test_product_creation():
    product = Product('Redmi Note 15 Pro', 1499.99, 'Laptop', 2)
    assert product.get_model == 'Redmi Note 15 Pro'
    assert product.get_price == 1499.99
    assert product.get_category == 'Laptop'
    assert product.check_in_storage == 2


test_product_creation()
