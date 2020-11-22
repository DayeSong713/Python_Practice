import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a+b

d = np.add(a, b)
print(c)
print(d)
e = b-a
print(e)
f = np.subtract(b, a)
print(f)

g = a*b
print(g)
h = np.multiply(a, b)
print(h)

i = b/a

print(i)
j = np.divide(b, a)
print(j)

list1 = [[1, 2], [3, 4]]
list2 = [[5, 6], [7, 8]]

k = np.array(list1)
l = np.array(list2)

m = np.dot(k, l)
print(m)


n = np.sum(k)
print(n)

o = np.sum(k, axis=0)
print(o)
p = np.sum(k, axis=1)
print(p)

q = np.prod(k)
print(q)
r = np.prod(k, axis=0)
print(r)
s = np.prod(k, axis=1)
print(s)
