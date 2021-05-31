from atm import ATM

bankAccounts = {
                "user1" : {"pin" : 5530, "savings" : 3600}, 
                "user2" : {"pin" : 8747, "savings" : 900},
                "user3" : {"pin" : 4055, "savings" : 12500},
               }

class Default_ATM(ATM):
        
    def __init__(self, money):
        self.blocked = False
        self.volume = 10000
        self.money = money


    def __str__(self):
            """Return a descriptive string for this instance, invoked by print() and str()"""
            return f'\nThis is a ATM : {self.money}, and  {self.volume} volume'

  
    def givemoney(self, moneyWithdraw):
        if(not self.blocked):
            print("userAccount?")
            usr = input()
            userAccount = bankAccounts.get(usr, False)
            if(userAccount):
                print("pin? --> ")
                pin = int(input())
                if(userAccount.get("pin", False) == pin):

                    if(userAccount.get("savings", False) >= moneyWithdraw):

                        if(self.money  >= moneyWithdraw):
                            self.money -= moneyWithdraw
                            print("Success")
                            bankAccounts[usr]["savings"] = userAccount["savings"] - moneyWithdraw
                            print(bankAccounts[usr]["savings"])
                        else:
                            print("Insufficient funds")
                            self.blockATM()
                        
                    else:
                        print("Not enought")
                else:
                    print("wrong pin")
            else: 
                print("wrong user")
        else: 
            print("ATM blocked, call incasators")

# atm1 = Default_ATM(10)
# atm1.givemoney(200)
# atm1.givemoney(200)
# atm1.callTheIncasator()
# atm1.givemoney(200)