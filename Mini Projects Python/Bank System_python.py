# Bank System :-

# Step 1 : Define the Blueprint (class) -

class Bank :

    def __init__(self,acc_no,bal):
        self.acc_no = acc_no
        self.bal = bal
        
# Step 2 : Add the Action Tool (amount) -

    def debit(self,amount):
        self.bal -= amount

        print("\n","="*10,"Welcome to SBI Bank","="*10)
        print("\n","=> Account Number: ",self.acc_no)
        print(" => Debited:",amount,"\n","=> Total Balance: ",self.bal)
        print("\n","="*10,"END","="*10)

# Step 2 : Add the Action Tool (amount) -

    def credit(self,amount):
        self.bal += amount
        
        print("\n","="*10,"Welcome to SBI Bank","="*10)
        print("\n","=> Account Number: ",self.acc_no)
        print(" => Credited:",amount,"\n","=> Total Balance: ",self.bal)
        print("\n","="*10,"END","="*10)

# Step 3 : The Main Execution (Outside the Class) -
acc_1 = Bank(1234,10000)
acc_1.debit(2000)
acc_1.credit(5100)