class BankAccount:
    def __init__(self , account_holder :str , initial_balance=0):
       self.__account_holder = account_holder
       self.__balance= initial_balance

    def deposit(self , amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds exist. Otherwise, raise an exception."""
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Return the current account balance."""
        return self.balance
    

    def get_account_holder(self):
        """Return the name of the account holder."""
        return self.account_holder

    def __str__(self):
        """Return a string representation of the account details."""
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

# Example usage:
account = BankAccount("eman hassan", 100)

# Depositing money
print(account.deposit(50))  # Output: 150

# Withdrawing money
try:
    print(account.withdraw(30))  # Output: 120
    print(account.withdraw(200))  # Should raise an exception
except Exception as e:
    print(f"Withdrawal failed: {e}")

# Getting balance
print(account.get_balance())  # Output: 120

# Getting account holder's name
print(account.get_account_holder())  # Output: eman hassan