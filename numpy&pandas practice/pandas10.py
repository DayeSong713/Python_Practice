import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame(np.random.randn(4, 3), columns=list('bde'),
               index=['seoul', 'busan', 'daegu', 'incheon'])


def format(x): return '%.2f' % x


s1 = df['e'].map(format)

print(s1.sort_index())

df2 = DataFrame(np.arange(8).reshape(2, 4), index=['abc', 'one'],
                columns=['d', 'a', 'b', 'c'])

print(df2)

print(df2.sort_index())
print(df2)

print(df2.sort_index(axis=1))

print(df2.sort_index(axis=1, ascending=False))


obj = Series([4, 7, -3, 1])

print(obj.sort_values())

obj2 = Series([4, np.nan, 8, np.nan, -10, 2])

print(obj2)

print(obj2.sort_values())

frame = DataFrame({'b': [4, 7, -5, 2], 'a': [0, 1, 0, 1]})

print(frame)

print(frame.sort_values(by='b'))
print(frame.sort_values(by=['a', 'b']))

obj3 = Series([7, -2, 7, 4, 2, 0, 4])
print(obj3)

print(obj3.rank())
print(obj3.rank(method='first'))


print(obj3.rank(ascending=False))

print(obj3.rank(ascending=False, method='min'))
