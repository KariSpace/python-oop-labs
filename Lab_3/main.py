from abc import ABC, abstractmethod
import random

bankAccounts = {
                "user1" : {"pin" : 5530, "savings" : 3600}, 
                "user2" : {"pin" : 8747, "savings" : 900},
                "user3" : {"pin" : 4055, "savings" : 12500},
               }


class ATM(ABC):

    @abstractmethod
    def __init__(self, money):
        self.blocked = False
        self.volume = 5000
        self.money = money

    # общие методы, который будут использовать все наследники этого класса
    def blockATM(self):
        self.blocked = True
        print("ATM was blocked")

    def unblockATM(self):
        self.blocked = False
        print("ATM unblocked")

    def callTheIncasator(self):
        self.money = self.volume
        self.unblockATM()

    # абстрактные методы, которые будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def givemoney(self):
        pass


class Default_ATM(ATM):
        
    def __init__(self, money):
        self.blocked = False
        self.volume = 10000
        self.money = money
  
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


class Secure_ATM(ATM):
        
    def __init__(self, money):
        self.blocked = False
        self.volume = 50000
        self.money = money
  
    def givemoney(self, moneyWithdraw):
        if(not self.blocked):
            print("userAccount?")
            usr = input()
            userAccount = bankAccounts.get(usr, False)
            if(userAccount):
                counter = 0
                while(not self.blocked):

                    if(counter == 2):
                        self.blockATM()
                        break
                    
                    print("pin? --> ")
                    pin = int(input())
                    if(userAccount.get("pin", False) == pin):
                        if(userAccount.get("savings", False) >= moneyWithdraw):
     
                            number = random.randint(1000,9999)
                            print(f'Your sms code: {number}')
                            code = int(input("code? --> "))

                            if(str(number) == str(code)):
                                if(self.money  >= moneyWithdraw):
                                    self.money -= moneyWithdraw
                                    print("Success")
                                    bankAccounts[usr]["savings"] = userAccount["savings"] - moneyWithdraw
                                    print(bankAccounts[usr]["savings"])
                                    break
                                else:
                                    print("Insufficient funds")
                                    self.blockATM()
                                    break
                            else:
                                 print("wrong code")
                        else:
                            print("Not enought")
                    else:
                        counter += 1
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

# atm2 = Secure_ATM(9000)
# atm2.givemoney(200)
# atm2.givemoney(200)
# atm2.callTheIncasator()
# atm2.givemoney(200)

