import pandas as pd
import numpy as np
from numpy import nan as NA
from pandas import Series, DataFrame

data = Series([1, NA, 3, 4, NA, 8])

print(data.dropna())


print(data.notnull())

print(data[data.notnull()])

data = DataFrame([[1, 5.5, 3], [1, NA, NA], [NA, NA, NA], [NA, 3.3, 3]])

print(data)

print(data.dropna())

print(data.dropna(how='all'))


data[4] = NA
print(data)

print(data.dropna(how='all', axis=1))

data2 = DataFrame([[1, 2, 3, NA], [NA, 33, 11, NA], [
                  11, NA, NA, NA], [43, NA, NA, NA]])

print(data2)

print(data2.dropna(thresh=2))

print(data2.fillna(0))

print(data2.fillna({1: 10, 3: 30}))

print(data2.fillna(method='ffill', limit=1))

data3 = Series([1, NA, 3.5, NA, 7])

print(data3.fillna(data3.mean()))

print(data3.fillna(data3.median()))
