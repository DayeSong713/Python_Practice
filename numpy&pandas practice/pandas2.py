import pandas as pd
from pandas import Series, DataFrame

obj = Series([1, 2, 3, 4])

print(obj)
print(obj.values)
print(obj.index)

obj2 = Series([4, 5, 6, 2], index=['d', 'c', 'e', 'f'])

print(obj2)

print(obj2['c'])

print(obj2[['d', 'f', 'c']])

print(obj2*2)
print('b' in obj2)
print('c' in obj2)

data = {'kim': 3400, 'hong': 2000, 'kang': 1000, 'lee': 2400}

obj3 = Series(data)

print(obj3)

name = ['woo', 'hong', 'kang', 'lee']
name2 = {'woo', 'hong', 'kang', 'lee'}

obj4 = Series(data, index=name)
print(obj4)

obj5 = Series(data, index=name2)
print(obj5)

print(pd.isnull(obj4))
print(pd.notnull(obj4))
