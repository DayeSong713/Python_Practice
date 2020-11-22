import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame(np.random.randn(4, 3), columns=list('bde'),
               index=['seoul', 'busan', 'daegu', 'Incheon'])

print(df)

print(np.abs(df))


def f(x): return x.max()-x.min()


print(df.apply(f))

print(df.apply(f, axis=1))


def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])


print(df.apply(f))


def format(x): return '%.2f' % x


print(df.applymap(format))

s1 = df['e']
print(s1.map(format))
