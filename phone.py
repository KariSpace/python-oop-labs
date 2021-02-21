class Mobile:                
    type = "Smartphone"  
    discount_rate = 0.2
    
    def __init__(self, company_name, model_name, color, price):
        self.company_name = company_name   
        self.model_name = model_name
        self.color = color
        self.price = price                
    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return 'This is a circle with radius of' +  self.company_name  
    
    def discount_price(self, discount):
        return self.price*(1-discount)
    
    @classmethod
    def set_discout_rate(cls, rate):
        cls.discount_rate = rate

    @staticmethod
    def is_shop_closed(day):
        if day.weekday() == 7:
            return False
        return True
        
if __name__ == '__main__':
    
    print()


    ## Create an instance of the Mobile Class.
    m1 = Mobile("Apple", "iPhone 11", "Blue", 780)
    m2 = Mobile("Samsung", "S10", "Red", 300)

    print(m2.discount_rate) # 0.5
    m1.set_discout_rate(0.5)
    
    print(m1) # 0.5
    print(m2.discount_rate) # 0.5


# Parent Classes vs Child Classes
# @staticmethod
# @classmethod
# operator overloading
# self._myvar = 2      # meant for internal use (private). 'Please' don't access directly
# self.__myvar__ = 5   # magic attribute
# Variables beginning with __ are not accessible outside the class except those ending with __
# Getter and Setter
# https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python1a_OOP.html