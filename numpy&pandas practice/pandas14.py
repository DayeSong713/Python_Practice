import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data1 = Series(np.random.randn(10))
print(data1)

data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 1, 2]])
print(data)

print(data.index)


print(data['b'])
print(data['a':'b'])
print(data[['a', 'd']])
print(data['a'][[1, 3]])
print(data[:, 2])
print(data[:, 3])

df = DataFrame(np.arange(12).reshape(4, 3),
               index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
               columns=[['seoul', 'busan', 'jeju'], ['red', 'green', 'red']])

print(df)

df.columns.names = ['cityName', 'color']

print(df)

df.index.names = ['key1', 'key2']
print(df)

print(df['seoul'])

df2 = df.swaplevel('key1', 'key2')

print(df2)

print(df.swaplevel(0, 1))

print(df.sum(level='key2'))

print(df.sum(level='color', axis=1))
