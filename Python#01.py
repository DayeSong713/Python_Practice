# 1.

money = int(input("받은 돈 : "))
price = int(input("물건 가격 : "))
tax = int(price*0.1)
change = money-price

print("받은 돈 : ", money)
print("물건 가격 : ", price)
print("세금 : ", tax)
print("거스름돈 : ", change)

# 2.

price500 = int(input("500원 동전 개수 : "))*500
price100 = int(input("100원 동전 개수 : "))*100
price50 = int(input("50원 동전 개수 : "))*50
price10 = int(input("10원 동전 개수 : "))*10
total = price500+price100+price50+price10
print("금액은 {}원입니다.".format(total))
