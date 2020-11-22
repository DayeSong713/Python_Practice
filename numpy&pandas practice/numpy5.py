import numpy as np

X = np.float32(1.0)
print(X)
print(type(X))
print(X.dtype)


z = np.arange(5, dtype='f')

print(z)

t = np.array([1, 2, 3], dtype='f')
print(t.dtype)

xx = np.int8(t)
print(xx.dtype)


bb = np.arange(10)
print(bb)

cc = np.arange(3, 10)
print(cc)

dd = np.arange(3, 10, dtype=np.float)
print(dd.dtype)

ee = np.arange(2, 3, 0.2)
print(ee)
