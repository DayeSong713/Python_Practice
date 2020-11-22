import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

print(obj['b': 'c'])

print(obj)
obj['b': 'c'] = 10
print(obj)

data = DataFrame(np.arange(16).reshape(4, 4), index=['seoul', 'busan', 'kwangju', 'daegu'],
                 columns=['one', 'two', 'three', 'four'])

print(data)

print(data['two'])

print(data[['one', 'two']])

print(data[2:])

print(data['three'] > 5)
print(data[data['three'] > 7])

print(data < 5)

print(data[data > 5])

data[data < 5] = 0
print(data)
