from atm import ATM
from default_atm import Default_ATM
from secure_atm import Secure_ATM

import collections.abc


bankAccounts = {
                "user1" : {"pin" : 5530, "savings" : 3600}, 
                "user2" : {"pin" : 8747, "savings" : 900},
                "user3" : {"pin" : 4055, "savings" : 12500}
               }
 

class MainBank:
    def __init__(self, atm=None):
        if (not atm):
            self.atm = []

    def __setitem__(self, key):
        self.atm.append(key)

    def __delitem__(self, key):
        self.atm.remove(key)

    def __len__(self):
        return len(self.atm)

    def __iter__(self):
        iter_atm = iter(self.atm)
        return iter_atm

    def __contains__(self, item):
        return True if item in self.atm else False




atm1 = Secure_ATM(9000)
atm2 = Default_ATM(200)
atm3 = Default_ATM(100)

bank = MainBank()
print(isinstance(bank, collections.abc.Container))
bank.__setitem__(atm1)
bank.__setitem__(atm2)
bank.__setitem__(atm3)


for i in range(bank.__len__()):
    print(bank.atm[i])

    
