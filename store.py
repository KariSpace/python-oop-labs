from datetime import date
CBLUE = '\33[104m'
CEND = '\033[0m'

class Store:

    phones_amount = 5

    def __init__(self, store_name):
        self.store_name = store_name

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'This is a store {self.store_name}. Now available {self.phones_amount} phones'

    @classmethod
    def buy_phone(cls):
        cls.phones_amount -= 1

    @classmethod
    def storrage_refill(cls, amount):
        cls.phones_amount += amount


    @staticmethod
    def is_shop_open():
        week = date.today().weekday()
        return not(week == 5 or week == 6)


if __name__ == '__main__':

    store1 = Store("Test Store")
    store2 = Store("KariStore")
    print(store1)


    # @staticmethod does not have access to an instance of the class, so
    # it can be called without instantiating the class
    print (f'\n\n{CBLUE}Static method:{CEND}')

    print(store1.is_shop_open()) 
    print(Store.is_shop_open())


    #  @classmethod bound to a class rather than an object. 
    # Class methods can be called by both class and object
    print(f'\n\n{CBLUE}Class method:{CEND}')

    print(store1.phones_amount) # 5
    store2.buy_phone() 
    print(store1.phones_amount) # 4

    Store.storrage_refill(10)
    print(store1.phones_amount) # 14
    print(f'{store1}\n{store2}')

    # delete class instance
    del store1, store2
