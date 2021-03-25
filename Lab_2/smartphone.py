import random
from mobilePhone import MobilePhone
from phone import Phone

class SmartPhone(MobilePhone):                
    
    def __init__(self, company, model, battery, screen, camera, operation_system):
        MobilePhone.__init__(self, company, battery, screen)


        self.model =  model
        self.screen =  screen
        self.type = "smart"
        self.camera =  camera
        self.operation_system =  operation_system

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'\nThis is a {self.type} phone, with battery : {self.battery}, and {self.screen} screen, {self.camera} camera, {self.operation_system} operation_system,'
        
    def update_os(self): 
        if random.choice([True, False]):
            print(f'Started updating your {self.operation_system}...\nDone!')
        else:
            print("Everything was updated")


m1 = SmartPhone("Samsung", "s20", 2500, "Full HD", "20MP", "Android")
m1.call("899-455-9095")
m1.send_sms("899-455-9095", "Hi! How are you?")
m1.update_os()
print(m1)