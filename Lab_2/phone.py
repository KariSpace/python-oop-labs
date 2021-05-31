import re
class Phone:              

    def __init__(self, company, battery):
        self.company = company   
        self.type = "antenna"
        self.battery = battery

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return f'\nThis is a {self.type} phone, with battery : {self.battery}' 

    def call(self, phone_number): 
        regex = r'\d{3}-\d{3}-\d{4}'

        if re.search(regex, phone_number):
            print(f'\nCalling to {phone_number}...')
        else:
            print("Invalid phone number")



m1 = Phone("Siemens", 500)
print(m1)
m1.call("349-345-0985")
print(m1)