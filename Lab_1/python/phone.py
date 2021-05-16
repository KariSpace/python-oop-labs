import re
from store import Store

CBLUE = '\033[1;34m'
CRED = '\033[1;31;48m'
CEND = '\033[0m'


class Phone:

    basic_color = "Grey"

    def __init__(self, company, model, price, hue):
        self.company = company
        self._model = model       # 'Please' don't access directly
        self.price = price
        self.color = hue + self.__class__.basic_color

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'\nThis is a {self.color} {self.company} {self._model} phone'

    def discount_price(self, discount):
        return self.price*(1-discount)

    def set_model(self, _model):
        """Setter for instance variable model"""
        match = re.search(r'[^0-9]', _model)
        if(match):
            raise ValueError('Shall be non-numeric')
        else:
            self._model = _model

    def get_model(self):
        """Getter for instance variable model"""
        return self._model


class Smartphone(Phone):

    def __init__(self, company, model, operation_system, price, color):
        super().__init__(company, model, price, color)

        self.operation_system = operation_system

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'\nThis is a {self.basic_color} Smartphone with {self.operation_system}'


if __name__ == '__main__':

    # Create an instance of the Mobile Class.
    m1 = Phone("Samsung", "x11", 780, "Dark")
    print(m1)
    m2 = Smartphone("Apple", "iPhone 11", "Mac OS", 780, "Blue")
    print(m2)

    store1 = Store("Test Store")
    store2 = Store("KariStore")
    print(store1)

    # @staticmethod does not have access to an instance of the class, so
    # it can be called without instantiating the class
    print(f'\n\n{CBLUE}Static method:{CEND}')

    print(store1.is_shop_open())
    print(Store.is_shop_open())

    #  @classmethod bound to a class rather than an object.
    # Class methods can be called by both class and object
    print(f'\n\n{CBLUE}Class method:{CEND}')

    print(store1.phones_amount)  # 5
    store2.buy_phone(m1)
    print(store1.phones_amount)  # 4

    Store.storrage_refill(10)
    print(store1.phones_amount)  # 14
    print(f'{store1}\n{store2}')

    # delete class instance
    del store1, store2
