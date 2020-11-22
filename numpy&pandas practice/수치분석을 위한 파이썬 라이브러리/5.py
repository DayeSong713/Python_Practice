import numpy as np

a = np.array([1, 2, 3])

print(type(a))

print(a.shape)

print(a[2])

a[0] = 10
print(a)

print(a.ndim)

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b.shape)
print(b)

arr1 = np.array([1, 2, 3])


print(b[1, 2])

print(b.ndim)
print(b.dtype.name)

print(a.itemsize)

arr = np.arange(12)
print(arr)

print(arr.reshape(4, 3))

arr = np.arange(12).reshape(3, 4)
print(arr)

print(type(arr))
print(arr.shape)
print(arr.itemsize)

print(np.zeros((3, 4)))

print(np.ones((3, 3)))

print(np.full((3, 3), 10))


print(np.eye(3))

c = np.random.random((2, 2))
print(c)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)

b = a[:2, :2]
print(b)

c = a[:2, 1:3]
print(c)

c[1, 1] = 20

print(a.ndim)

arr1 = np.array([1, 2, 3])

print(arr1)
print(arr1.shape)

arr2 = np.array([[1, 2, 3]])
print(arr2.shape)
print(arr2.ndim)

bb = a[1, :]
print(bb)

print(bb.ndim, bb.shape)

bb2 = a[1:2, :]

print(bb2.ndim, bb2.shape)

a = np.array([[1, 2], [3, 4], [5, 6]])

print(a)

print(a[[0, 1, 2], [0, 1, 0]])

ia = a[[0, 1, 2], [0, 1, 0]]

print(ia.shape)

a = np.arange(1, 10)
print(a)

b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(b)

idx = np.array([0, 0, 0, 0, 1, 1, 1, 2, 2, 2])

print(idx)

print(a[idx])

a = np.array([[1, 2], [3, 4], [5, 6]])

b = a[[0, 1, 2], [0, 1, 0]]
print(b)

c = a[[0, 1], [0, 1]]
print(c)

d = a[:, [False, True]]

print(a)
print(d)

e = a[[2, 0, 1], :]

print(e)
