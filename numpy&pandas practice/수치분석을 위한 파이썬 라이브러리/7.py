import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))

print(np.dot(v, w))

print(x.dot(v))
print(np.dot(x, v))
print(np.dot(v, x).ndim)


print(x.dot(y))
print(np.dot(x, y).ndim)

xx = np.array([[1, 2], [3, 4]])
yy = np.array([1, 2])
print(np.sum(x))

print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

print(xx.T)

print(yy.T)

g = np.empty((4, 3))

print(g)




