import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

idx = np.array([0, 2, 0, 1])

print(a[np.arange(4), idx])

a[np.arange(4), idx] *= 2

print(a)


b = np.arange(10)

print(b)

print(b[b % 2 == 0])

x = np.array([[1, 2], [3, 4]], dtype=np.float64)

y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print(x, y)

print(x+y)

print(np.add(x, y))

print(x-y)
print(np.subtract(x, y))

print(x*y)
print(np.multiply(x, y))

print(x/y)
print(np.divide(x, y))

print(np.sqrt(y))

print(x == 2)

print(x[x < 3])

print(y > 6)

print((x>3)&(y>6))
