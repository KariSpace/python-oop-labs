from datetime import date


class Store:

    phones_amount = 5

    def __init__(self, store_name):
        self.store_name = store_name

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'This is a store {self.store_name}. Now available {self.phones_amount} phones'

    @classmethod
    def buy_phone(cls, rate):
        cls.phones_amount -= 1

    @staticmethod
    def is_shop_open():
        week = date.today().weekday()
        return not(week == 5 or week == 6)


if __name__ == '__main__':

    store1 = Store("KariStore")
    print(store1)

    # @staticmethod does not have access to an instance of the class, so
    # it can be called without instantiating the class
    print(store1.is_shop_open()) 
    print(Store.is_shop_open())
