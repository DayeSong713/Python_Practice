import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(obj)

obj2 = obj.drop('c')
print(obj2)

obj3 = obj.drop(['b', 'd'])
print(obj3)

df = DataFrame(np.arange(16).reshape(4, 4), index=[
               'a', 'b', 'c', 'd'], columns=[1, 2, 3, 4])
print(df)

df2 = df.drop(['a', 'b'])

print(df2)

df3 = df.drop(3, axis=1)
print(df3)

df4 = df.drop([3, 4], axis=1)

print(df4)
