import pandas as pd
from pandas import Series, DataFrame
import numpy as np

s1 = Series([5, 6, -1, 2], index=['a', 'c', 'd', 'e'])

s2 = Series([3, 4, -1, 2, 7], index=['a', 'c', 'e', 'f', 'g'])

print(s1+s2)

df1 = DataFrame(np.arange(9).reshape(3, 3), columns=list('bcd'),
                index=['seoul', 'busan', 'kwangju'])

df2 = DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'),
                index=['Incheon', 'seoul', 'busan', 'suwon'])

print(df1)
print(df2)
print(df1+df2)

df3 = DataFrame(np.arange(12).reshape(3, 4), columns=list('abcd'))
df4 = DataFrame(np.arange(20).reshape(4, 5), columns=list('abcde'))

print(df3)
print(df4)

print(df3+df4)

print(df3.add(df4, fill_value=0))

print(df3.reindex(columns=df4.columns, fill_value=0))
