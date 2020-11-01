import random


class GoodStock:
    def __init__(self, code, amount):
        self.code = code
        self.amount = amount
        print("상품 코드 : ", self.code)
        print("재고 수량 : ", self.amount)

    def addStock(self, adding_amount):
        self.amount += adding_amount
        print("재고 수량 : ", self.amount)


good1_name = input("상품 코드를 입력하세요 : ")
good1_amount = int(input("재고 수량을 입력하세요 : "))

good1 = GoodStock(good1_name, good1_amount)

good1_adding_amount = int(input("추가할 수량을 입력하세요 : "))
good1.addStock(good1_adding_amount)


class Account:
    def __init__(self, accountNo, ownerName, balance):
        self.accountNo = accountNo
        self.ownerName = ownerName
        self.balance = balance

    def deposit(self, amount):
        print("{}님 계좌에 {}원을 입금합니다.".format(self.ownerName, amount))
        self.balance += amount

    def withdraw(self, amount):
        print("{}님 계좌에서 {}원을 인출합니다.".format(self.ownerName, amount))
        self.balance -= amount

    def printAccount(self):
        print("--계좌 정보--")
        print("계좌번호 : ", self.accountNo)
        print("예금주 이름 : ", self.ownerName)
        print("잔액 : ", self.balance)


obj1 = Account("111-222-3333333", "송다예", 50000)
obj2 = Account("555-666-7777777", "손이안", 10000)

obj1.deposit(10000)
obj2.withdraw(5000)

obj1.printAccount()
obj2.printAccount()


class FourCal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b


num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))

obj3 = FourCal(num1, num2)

print("두 수를 더한 값 : ", obj3.add())
print("두 수를 뺀 값 : ", obj3.sub())
print("두 수를 곱한 값 : ", obj3.mul())
print("두 수를 나눈 값 : ", obj3.div())


# 4


class Dice:
    def __init__(self):
        self.num = 1
        print("--주사위 생성완료. 초기 상태는 1입니다.--")

    def roll(self):
        self.num = random.randrange(1, 7)

    def toString(self):
        print("현재 주사위 상태는", self.num)


dice1 = Dice()

dice1.roll()
dice1.toString()
