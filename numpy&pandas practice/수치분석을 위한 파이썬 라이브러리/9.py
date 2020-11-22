import numpy as np

a = np.array([[1, 2], [3, 4]])
b = 10

print(a+b)
print(a*b)

a = np.array([1, 2, 3, 4])
b = np.array([1, 2])

x = np.arange(3)
y = 5

print(x+y)

c = np.ones((3, 3))
d = np.array([0, 1, 2])
d = np.arange(3)

print(c)
print(d)
print(c+d)

e = np.arange(3).reshape(3, 1)
f = np.arange(1, 4)
print(e+f)

g = np.array([[[0, 1], [2, 3], [4, 5], [6, 7]], [[8, 9], [10, 11], [
             12, 13], [14, 15]], [[16, 17], [18, 19], [20, 21], [22, 23]]])


print(g)

h = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])

print(h)

print(g+h)

print(g.dtype)

i = np.array([1, 2, 3], dtype="int")
print(i.dtype)

j = np.array([1, 2, 3], dtype="f")
print(j)

k = np.array([1, 2, 3], dtype="U")
print(k.dtype)

print(k[1]+k[2])

print(np.array([0, 1, -1, 0])/np.array([1, 0, 0, 0]))
