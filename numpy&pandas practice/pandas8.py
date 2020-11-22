import pandas as pd
from pandas import Series, DataFrame
import numpy as np

arr = np.arange(12.).reshape(3, 4)

print(arr)

print(arr[0])

print(arr-arr[0])

df = DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'),
               index=['seoul', 'kwangju', 'daegu', 'Incheon'])

print(df)

s2 = Series(range(3), index=list('bef'))
print(s2)

print(df+s2)

s3 = df['d']

print(s3)

print(df+s3)

print(df.add(s3, axis=0))

print(df.sub(s3, axis=0))
