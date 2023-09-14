class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount > self.__account_balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Create an instance of BankAccount
my_account = BankAccount("1234567890", "John Doe", 1000.00)

# Test deposit and withdrawal functionality
my_account.display_balance()
my_account.deposit(500.0)
my_account.withdraw(200.0)
my_account.display_balance ()