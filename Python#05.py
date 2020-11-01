# 1
'''with open("file1.txt", "w") as file:
    for i in range(100):
        file.write("{}번째 줄입니다.\n\n".format(i+1))


# 2

name = input("이름을 입력하세요 : ")
age = input("나이를 입력하세요 : ")
hobby = input("취미를 입력하세요 : ")

with open("file2.txt", "w") as file:
    file.write("이름: {}\n\n".format(name))
    file.write("나이: {}\n\n".format(age))
    file.write("취미: {}".format(hobby))

print("파일에 입력을 완료했습니다.")'''

# 3

with open("file2.txt", "r") as file:
    for line in file:
        print("***", line)
