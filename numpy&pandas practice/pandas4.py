import pandas as pd
import numpy as np
from pandas import Series, DataFrame

'''obj = Series(range(3), index=['a', 'b', 'c'])

print(obj)

idx = obj.index

print(idx)

print(idx[1])

print(idx[1:])

idx[1] = 'd'

print(idx)

index2 = pd.Index(np.arange(3))
print(index2)

obj2 = Series([2.3, 4.3, -4.1, 3.5], index=['d', 'b', 'a', 'c'])
print(obj2)


obj3 = obj2.reindex(['a', 'b', 'c', 'd', 'e'])

print(obj3)

obj4 = obj2.reindex(['a', 'b', 'c', 'd', 'e', 'f'], fill_value=0.0)
print(obj4)

obj5 = Series(['blue', 'red', 'yellow'], index=[0, 2, 4])
print(obj5)

obj6 = obj5.reindex(range(6), method='ffill')
print(obj6)'''

df = DataFrame(np.arange(9).reshape(3, 3), index=[
               'a', 'b', 'd'], columns=['x', 'y', 'z'])
print(df)

df2 = df.reindex(['a', 'b', 'c', 'd'])
print(df2)
col = ['w', 'm', 'n']
print(df2.reindex(columns=col))

col2 = ['x', 'y', 'w', 'z']
print(df2.reindex(columns=col2))


df3 = df.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=col2)
print(df3)
