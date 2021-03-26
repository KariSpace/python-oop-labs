from atm import ATM
import random
bankAccounts = {
                "user1" : {"pin" : 5530, "savings" : 3600}, 
                "user2" : {"pin" : 8747, "savings" : 900},
                "user3" : {"pin" : 4055, "savings" : 12500},
               }

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

atm1 = Secure_ATM(9000)
atm1.givemoney(200)
atm1.givemoney(200)
atm1.callTheIncasator()
atm1.givemoney(200)