import numpy as np

a = np.ones((2, 3))

b = np.zeros((2, 2))

print(np.hstack([a, b]))

c = np.ones((2, 3))
d = np.zeros((3, 3))
print(np.vstack([c, d]))

e = np.ones((3, 4))
f = np.zeros((3, 4))
g = np.dstack([e, f])
print(g)
print(g.shape)

h = np.stack([e, f])
print(h, h.shape)

i = np.stack([e, f], axis=1)
print(i, i.shape)

j = np.stack([e, f], axis=2)
print(j, j.shape)

k = np.array([1, 2, 3])
l = np.array([4, 5, 6])

print(np.r_[k, l])

print(np.c_[k, l])

m = np.array([[0, 1, 2], [11, 22, 33]])

n = np.tile(m, (2, 1))

print(n)
