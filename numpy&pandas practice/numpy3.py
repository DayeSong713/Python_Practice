import numpy as np

list = [[1, 2, 3],
        [4, 5, 6], [7, 8, 9]]

arr = np.array(list)

a = arr[0:2, 0:2]

print(a)

b = arr[1:, 1:]
print(b)

c = arr[[0, 1], [0, 1]]
print(c)

d = arr[[1, 2, 0], [2, 0, 1]]
print(d)

b_arr = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False]
])

n = arr[b_arr]
print(n)

b_arr2 = (arr % 2 == 1)
n2 = arr[b_arr2]
print(n2)
print(b_arr2)

n3 = arr[arr % 2 == 0]
print(n3)
