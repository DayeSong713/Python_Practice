import numpy as np

list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a)

print(a.shape)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)
print(b[0, 0])


aa = np.zeros((2, 2))
print(aa)
print(aa.shape)

print(type(aa))

bb = np.ones((2, 3))
print(bb)

cc = np.full((2, 3), 10)
print(cc)

dd = np.eye(3)
print(dd)

ee = np.array(range(20)).reshape((5, 4))

print(ee)
