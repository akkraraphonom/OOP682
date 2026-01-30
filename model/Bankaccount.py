class BankAccount:
    def __init__ (self , balance):
        self.balance = balance

    def __add__(self , other):
        if isinstance(other , BankAccount):
            new_balance = self.balance + other.balance
            new_account = BankAccount(new_balance) 
            return new_account
        return None

    def __str__ (self):
        return f"BankAccount : {self.balance:,.2f}"

my_account = BankAccount(1000)
your_account = BankAccount(500)

our_account = my_account + your_account
print(our_account)