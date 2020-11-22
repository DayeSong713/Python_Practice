import numpy as np

d = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],
              [[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]]])

print(len(d))

print(len(d[0]))

print(len(d[0][0]))

c = np.ones((2, 3, 4), dtype='i')
print(c)

k = np.ones_like(c, dtype="f")
print(k)

cc = np.copy(c)

print(c)

z = np.zeros((2, 3, 2))
print(z)

zz = np.ones_like(z)
print(zz)

aa = np.arange(3, 11, 2)
print(aa)
