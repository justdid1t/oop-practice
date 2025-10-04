class BankAccount:
    min_deposit = 100
    min_withdrawal = 100
    max_withdrawal = 100000

    def __init__(self, name, initial_deposit):
        self.name = name
        self.__balance = initial_deposit

    def deposit(self, amount):
        if amount < self.min_deposit:
            print(f"Minimum deposit: {self.min_deposit}\n")
        else:
            self.__balance += amount
            print(f"Successful deposit of {amount}\n")

    def withdraw(self, amount):
        if amount < self.min_withdrawal:
            print(f"Minimum withdrawal: {self.min_withdrawal}\n")
        elif amount > self.max_withdrawal:
            print(f"Maximum withdrawal at once: {self.max_withdrawal}\n")
        elif amount > self.__balance:
            print("Insufficient balance!\n")
        else:
            self.__balance -= amount
            print(f"Successful withdrawal of {amount}\n")

    def check_balance(self):
        print(f"Your current balance is: {self.__balance}\n")

    def get_balance(self):
        return self.__balance


# test
ac1 = BankAccount("Nur", 1000)
ac2 = BankAccount("John", 10000)

ac1.check_balance()
ac1.__balance = 0  # will not affect actual private variable
ac1.check_balance()

ac1.deposit(105)
ac1.check_balance()

ac1.withdraw(1000)
ac1.check_balance()
