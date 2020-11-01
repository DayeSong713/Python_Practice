# 1
'''amountT = int(input("티셔츠 개수 입력 : "))
amountS = int(input("스웨터 개수 입력 : "))
total = amountT*10000 + amountS*30000
if(total <= 100000):
    print("합계 : ", int(total*0.95), "원")
else:
    print("합계 : ", int(total*0.85), "원")

# 2

num1 = int(input("두 개의 양의 정수를 입력하세요 :\n"))
num2 = int(input(""))
bigger = num1
num = "홀"
if num1 < num2:
    bigger = num2
if bigger % 2 == 0:
    num = "짝"

print("{} 이 큰 수이고, {}수이다.".format(bigger, num))


# 3

print("삼각형 판단")
a = int(input("삼각형으로 만들고자 하는 세 변의 길이 입력(가장 큰 수를 마지막에 입력):\n"))
b = int(input(""))
c = int(input(""))

if a+b <= c:
    print("삼각형이 아니다")

elif a == b and b == c:
    print("정삼각형이다.")

elif (a == b or b == c) and a**2+b**2 == c**2:
    print("이등변 직각삼각형이다.")

elif a**2+b**2 == c**2:
    print("직각삼각형이다.")

elif a == b or b == c:
    print("이등변삼각형이다.")

else:
    print("일반 삼각형이다.")


# 4
a = int(input("세 개의 양의 정수를 입력하세요 : \n"))
b = int(input(""))
c = int(input(""))
nums = [a, b, c]
if(a+b+c) % 2 == 1:
    print(a+b+c)

else:
    nums.sort(reverse=True)
    print(nums[0])

# 5
'''
# 6
password = input("비밀번호 입력 : ")
if len(password) < 5:
    stability = "Bad"
elif len(password) >= 9:
    stability = "Good"
else:
    stability = "Normal"

print("Your Password: ", stability)
