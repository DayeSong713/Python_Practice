import numpy as np

a = np.array([1, 10, 100])

print(a.argmax())

print(a.sum(), np.median(a), a.std())

b = np.array([1, 2, 3, 1])

print(np.median(b))

print(np.all([True, True, False]))

print(np.any([True, False]))

c = np.array([[1, 1], [2, 2]])

print(c.sum(axis=0))

print(c.sum(axis=1))

d = np.array([[4, 3, 5, 7], [1, 9, 8, 2], [2, 5, 1, 3]])

print(np.sort(d))
print(np.sort(d,axis=0))


e=np.array([55,33,11,22])
f=np.argsort(e)


print(f)
print(e[f])