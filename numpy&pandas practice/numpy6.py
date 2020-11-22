import numpy as np
a = np.array([[1, 2], [3, 4]])
b = 10
c = a*b
print(c)
d = np.array([10, 20])
e = a*d
print(e)


f = np.array([[11, 21], [34, 43], [0, 9]])
print(f)

for row in f:
    print(row)


'''평탄화: flatten() 2차원배열을 1차원배열로'''

f = f.flatten()
print(f)

print(f[np.array([1, 3, 5])])

print(f[f > 20])

print(f > 25)
