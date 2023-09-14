class BankAccount:
    def __init__(self, acc_num, acc_holder, initial_balance=0.0):
        self.__acc_num = acc_num
        self.__acc_holder = acc_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account balance for {self.__acc_holder} (Account #{self.__acc_num}): ${self.__balance}"
account = BankAccount("12345", "John Doe", 1000.0)
print(account.display_balance())
print(account.deposit(500.0))
print(account.withdraw(200.0))
print(account.withdraw(1500.0)) 