class BalanceError(Exception):
    value = "Sorry you only have $%6.2f in your account"


class BankAccount:
    def __init__(self, initial_amount):
        self.balance = initial_amount
        print("Account created with balance %5.2f" % self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            raise BalanceError(BalanceError.value % self.balance)

    def check_balance(self):
        return self.balance

    def transfer(self, amount, account):
        try:
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceError:
            print(BalanceError.value % self.balance)


class InterestAccount(BankAccount):
    def __init__(self, initial_amount, interest=0.03):
        BankAccount.__init__(self, initial_amount)
        self.interest = interest

    def deposit(self, amount):
        BankAccount.deposit(self, amount)
        self.balance = self.balance * (1 + self.interest)


class ChargingAccount(BankAccount):
    def __init__(self, initial_amount, fee=3):
        BankAccount.__init__(self, initial_amount)
        self.fee = fee

    def withdraw(self, amount):
        BankAccount.withdraw(self, amount + self.fee)
