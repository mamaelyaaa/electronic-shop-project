from src.modules.cart import ShoppingCart


class Customer:

    def __init__(self, name: str, surname: str, email: str, phone: str, cart: ShoppingCart = None):
        self._name = name
        self._surname = surname
        self.get_email = email
        self.get_phone = phone
        self.cart = cart

    def place_an_order(self, cart: ShoppingCart):
        pass

    def get_history_of_orders(self):
        pass

    @property
    def get_name(self):
        return self._name

    @property
    def get_surname(self):
        return self._surname

    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def get_email(self, s: str):
        if '@gmail.com' in s or '@mail.ru' in s or '@bk.com' in s and s.index('@') > 0:
            self._email = s
        else:
            raise ValueError('Неправильный формат электронной почты')

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

    @property
    def get_cart(self):
        return self.cart
