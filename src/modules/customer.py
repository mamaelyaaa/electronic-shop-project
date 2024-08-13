from src.modules.cart import ShoppingCart
from src.modules.order import Order


class Customer:

    def __init__(self, name: str, email: str, phone: str):
        self.get_name = name
        self.get_email = email
        self.get_phone = phone
        self._order_cache: list[Order] = []

    def place_an_order(self, cart: ShoppingCart):
        if not cart.get_goods:
            raise ValueError('Корзина пуста. Пожалуйста, добавьте товары для оформления заказа')

        order = Order(self, cart.get_goods, cart.get_price())
        self._order_cache.append(order)
        return order

    def get_history_of_orders(self):
        return self._order_cache

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def get_name(self, name: str):
        if all(word.split() for word in name.split() if word.isalpha()) and len(name.split()) >= 1:
            self._name = name
        else:
            raise ValueError('Wrong name format')

    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def get_email(self, s: str):
        if '@gmail.com' in s or '@mail.ru' in s or '@bk.com' in s or '@example.com' in s and s.index('@') > 0:
            self._email = s
        else:
            raise ValueError('Wrong email format')

    @property
    def get_phone(self):
        return self._phone

    @get_phone.setter
    def get_phone(self, phone: str):
        valid_nums = ''.join([chr(i) for i in range(ord('0'), ord('9') + 1)] + ['+'])

        if len(phone) == 12 and phone[0] == '+' and all(i in valid_nums for i in phone):
            self._phone = phone
        else:
            raise ValueError('Неправильный формат номера телефона')
