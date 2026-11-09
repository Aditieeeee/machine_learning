class Atm:
   balance=0
   def activate_card(self):
        print("welcome to the bob bank")
       
        self.pin=int(input("create your pin"))
        print("your pin has been created")

   def checkbalance(self):
       print("check balance section")
       temp=int(input("enter your pin:"))
       if temp==self.pin:
            print("correct pin")
            print("the balance is :",self.balance)
       else:
           print("pin daal sahi")     

   def addamount(self):
        print("add amount section")
        temp=int(input("enter your pin:"))
        if temp==self.pin:
            amount=int(input("enter the amount"))
            if amount>0:
              print("valid amount")
              
              self.balance=self.balance+amount
              print("amount added")
              
            else:
                print("enter correct amount")   
        else:
            print("bloody thief wrong pin")
            
   def withdraw(self):
        print("money withdrwal section")
        temp=int(input("enter your pin:"))
        if temp==self.pin:
           print("checking balance......")
           amount=int(input("enter the amount"))
           if amount<self.balance:
             print("valid amount +++")
             self.balance=self.balance-amount
             print("withdrwal done")
             
             
           else:
               print("balance is less than withdrwal amount")
        else:
           print("wrong pin")
                 
 