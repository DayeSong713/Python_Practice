# 1

import random
price = 300
coffee = 10

while coffee > 0:
    money = int(input("돈을 넣어주세요: "))
    if money < 300:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    else:
        out = money//price
        rest = money % price
        coffee -= out
        print("거스름돈 {}원을 주고 커피를 {}잔 줍니다".format(rest, out))
        print("남은 커피의 양은 {}입니다.".format(coffee))

print("커피가 다 떨어졌습니다. 판매를 중지합니다.")

# 2

student = [90, 30, 58, 61, 100]

for i in range(len(student)):
    if student[i] > 60:
        result = "합격"
    else:
        result = "불합격"
    print("{}번 학생은 {}입니다.".format(i+1, result))


# 3

student = [90, 30, 58, 61, 100]

for i in range(len(student)):
    if student[i] > 60:
        print("{}번 학생 축하합니다. 합격입니다.".format(i+1))

# 4

rannum = random.randrange(1, 99)
try1 = 1
ans = 0
while ans != rannum:
    ans = int(input("정답을 추측해보세요 : "))
    if ans == rannum:
        print("축하합니다! 시도 횟수는 {}번입니다.".format(try1))
    elif ans > rannum:
        print("다운")
        try1 += 1
    else:
        print("업")
        try1 += 1


# 5

sum = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 4 == 0:
        continue
    else:
        sum += i
print(sum)
