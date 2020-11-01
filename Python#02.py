# 1
print("# if 조건문에0 넣기")
if 0:
    print("0은True로변환됩니다.")
else:
    print("0은False로변환됩니다.")
    print()


print("# if 조건문에빈문자열넣기")
if "":
    print("빈문자열은True로변환됩니다.")
else:
    print("빈문자열은False로변환됩니다.")

# 2-1
year = int(input("태어난 해를 입력해주세요> "))

if year % 12 == 0:
    print("원숭이 띠입니다.")
elif year % 12 == 1:
    print("닭 띠입니다.")
elif year % 12 == 2:
    print("개 띠입니다.")
elif year % 12 == 3:
    print("돼지 띠입니다.")
elif year % 12 == 4:
    print("쥐 띠입니다.")
elif year % 12 == 5:
    print("소 띠입니다.")
elif year % 12 == 6:
    print("호랑이 띠입니다.")
elif year % 12 == 7:
    print("토끼 띠입니다.")
elif year % 12 == 8:
    print("용 띠입니다.")
elif year % 12 == 9:
    print("뱀 띠입니다.")
elif year % 12 == 10:
    print("말 띠입니다.")
else:
    print("양 띠입니다.")


# 2-2
year = int(input("태어난 해를 입력해 주세요 : "))
index = year % 12
animal = ["원숭이", "닭", "개", "돼지", "쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양"]
print("{}띠입니다.".format(animal[index]))

# 3-1

num1 = int(input("숫자를 입력하세요 : "))
num2 = int(input("숫자를 입력하세요 : "))
num3 = int(input("숫자를 입력하세요 : "))

minnum = num1
if num1 > num2:
    minnum = num2
    if num2 > num3:
        minnum = num3
elif num1 > num3:
    minnum = num3

print("가장 작은 수는 {}입니다.".format(minnum))

# 3-2

nums = []
nums.append(int(input("숫자를 입력하세요 : ")))
nums.append(int(input("숫자를 입력하세요 : ")))
nums.append(int(input("숫자를 입력하세요 : ")))
nums.sort()
print("가장 작은 수는 {}입니다.".format(nums[0]))

# 4

height = int(input("키를 입력하세요 : "))
weight = int(input("몸무게를 입력하세요 : "))
standard = (height-100)*0.9
if standard > weight:
    print("저체중입니다.")
elif standard < weight:
    print("과체중입니다.")
else:
    print("표준 체중입니다.")
