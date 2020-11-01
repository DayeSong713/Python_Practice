# 1
# 리스트a 선언
a = [1, 2, 3, 1]
# 리스트a에서 1의 개수는?
print(a.count(1))

# 1-2

list_a = [1, 2, 3, 1]
cnt = 0
for i in list_a:
    if(i == 1):
        cnt += 1
print("1의 개수는 {}개 입니다.".format(cnt))

# 2-1

list_1 = [1, 3, 5, 4, 2]
list_1[0] = 5
list_1[1] = 4
list_1[2] = 3
list_1[3] = 2
list_1[4] = 1
print(list_1)

# 2-2

list_2 = [1, 3, 5, 4, 2]
list_2.sort(reverse=True)
print(list_2)


# 3

t1 = (1, 2, 3)
t2 = (4,)
t3 = t1+t2
print(t3)
