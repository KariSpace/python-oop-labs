import re
from store import Store

CBLUE = '\033[44m'
CRED = '\033[1;31;48m'
CEND = '\033[0m'



class Phone:              

    color = "Grey"

    def __init__(self, company_name, model_name, price, color_name):
        self.company_name = company_name   
        self._model_name = model_name       # 'Please' don't access directly
        self.price = price   
        self.color_name = color_name + self.__class__.color

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'\nThis is a {self.color_name} {self.company_name} {self._model_name} phone' 

    def discount_price(self, discount):
        return self.price*(1-discount)
    
    def set_model_name(self, _model_name):
        """Setter for instance variable model_name"""
        match = re.search(r'[^0-9]', _model_name)
        if(match):
            raise ValueError('Radius shall be non-numeric')
        else:
            self._model_name = _model_name

    def get_model_name(self): 
        """Getter for instance variable model_name"""
        return self._model_name



class Smartphone(Phone):                
    
    def __init__(self, company_name, model_name, operation_system, price, color_name):
        super().__init__(company_name, model_name, price, color_name)

        self.operation_system =  operation_system

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'\nThis is a {self.color} Smartphone with {self.operation_system}'


if __name__ == '__main__':
    
    ## Create an instance of the Mobile Class.
    m1 = Phone("Samsung", "x11", 780, "Dark")
    print(m1)
    m2 = Smartphone("Apple", "iPhone 11", "Mac OS", 780, "Blue")
    print(m2)


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
    store2.buy_phone(m1) 
    print(store1.phones_amount) # 4

    Store.storrage_refill(10)
    print(store1.phones_amount) # 14
    print(f'{store1}\n{store2}')

    # delete class instance
    del store1, store2
