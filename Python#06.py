# 1
'''class MyError(Exception):
    pass


def animal(ani):
    if ani == '바나나':
        raise MyError()
    print(ani)


try:
    animal("강아지")
    animal("바나나")
except MyError:
    print("동물이 아닙니다.")


# 2
intnum = input("정수를 입력하세요 ")
try:
    print(int(intnum))
except:
    print("정수가 아닙니다.")
'''

# 3
nums = []
sum = 0
for i in range(5):
    try:
        newnum = int(input("정수를 5개 입력하세요. 정수가 아니면 더하지 않습니다."))
        nums.append(newnum)
    except:
        print("정수로 변환할 수 없습니다.")

for j in nums:
    sum += j

print("정수 합 : ", sum)
