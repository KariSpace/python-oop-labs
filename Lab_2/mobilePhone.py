import re
from phone import Phone

class MobilePhone(Phone):                
    
    def __init__(self, company, battery, screen):
        super().__init__(company, battery)

        self.screen =  screen
        self.type = "mobile"

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'\nThis is a {self.type} phone, with battery : {self.battery}, and  {self.screen} screen'
        
    def send_sms(self, phone_number, sms_text): 
        regex = r'\d{3}-\d{3}-\d{4}'
        if re.search(regex, phone_number):
            print(f'\nSending sms to {phone_number} with text: {sms_text}')
        else:
            print("Cant send sms to invalid phone number")


# m1 = MobilePhone("Samsung", 900, "collor")
# m1.call("899-455-9095")
# m1.send_sms("899-455-9095", "Hi! How are you?")
# print(m1)