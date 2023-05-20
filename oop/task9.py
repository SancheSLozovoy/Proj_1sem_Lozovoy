class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def depos(self, amount):
        if amount < 0:
            print('Нельзя внести отрицат. сумму')
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Нельзя снять отрицательную сумму")
        elif self.__balance < amount:
            print("Недостаточно средст для снтия")
        else:
            self.__balance -= amount


acc = BankAccount(1000, 'alex')
print(acc.get_balance())

acc.depos(100)
print(acc.get_balance())

acc.withdraw(200)
print(acc.get_balance())