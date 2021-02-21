class Store :    
        
    discount_rate = 0.2
    
    def __init__(self, store_name, phones_amount):
        self.store_name = store_name   
        self.phones_amount = phones_amount
             
    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'This is a store {self.store_name}. Now available {self.phones_amount} phones' 
    
    # def discount_price(self, discount):
    #     return self.price*(1-discount)
    
    @classmethod
    def buy_phone(cls, rate):
        cls.discount_rate = rate

    @staticmethod
    def is_shop_closed(day):
        print(day.weekday())
        if (day.weekday() == 7 | day.weekday() == 6):
            return False
        return True
        
if __name__ == '__main__':
    
    store1 = Store()
    print()
