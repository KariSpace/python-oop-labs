import re
from beeprint import pp

clases = {}

class MyMetaclass(type):
    def __new__(cls, clsname, superclasses, attributedict):
      #   print("clsname: ", clsname)
      #   print("superclasses: ", superclasses)
      #   print("attributedict: ", attributedict)
         clases[clsname] = {
           "methods" : [*attributedict],
           "methods_amount" : len([*attributedict])
         }

         return type.__new__(cls, clsname, superclasses, attributedict)
         

class ATM(metaclass=MyMetaclass):

    def blockATM(self):
        self.blocked = True
        print("ATM was blocked")

    def unblockATM(self):
        self.blocked = False
        print("ATM unblocked")

    def callTheIncasator(self):
        self.money = self.volume
        self.unblockATM()


class Phone(metaclass=MyMetaclass):

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


pp(clases)