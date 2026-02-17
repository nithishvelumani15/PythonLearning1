class User:
    user_count = 0
    def __init__(self,username,email):
        self.username = username
        self.email = email
        User.user_count += 1
    def display(self):
        print(f"Username: {self.username}, Email: {self.email}")
   
class BankAccount:
    MIN_BALANCE = 100
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self._balance = balance
    def display(self):
        print(f"{self.owner}'s balance is {self._balance}")
    def deposit(self,amount):
        if(amount>0):
            self._balance+=amount
            print(f"{self.owner}'s new balance : {self._balance}")
            if(BankAccount.is_valid_interest_rate(5)):
                print(f"{5} is valid")
        else:
            print("Deposit amount should be more than 0")
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <=5

owner1 = BankAccount("Nithish",100)
owner1.deposit(100)

