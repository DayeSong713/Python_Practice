'''기술 통계 계산
pandas는 일반적인 수학/통계 메서드를 가지고 있다.
pandas의 메서드는 처음부터 누락된 데이터를 제외하도록 설계되어 있다.'''

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
               index=['a', 'b', 'c', 'd'], columns=['one', 'two'])

print(df)

'''sum()메서드는 각 컬럼의 값을 더해서 Series 객체를 반영한다.'''
print(df.sum())

print(df.sum(axis=1))

print(df.sum(axis=1, skipna=False))

print(df.idxmax())

print(df.cumsum())

s1 = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

print(s1)

unique = s1.unique()
print(unique)

cnt = s1.value_counts()
print(cnt)


mask = s1.isin(['b', 'c'])

print(mask)

print(s1[mask])

data = DataFrame({'Q1': [1, 3, 4, 3, 4], 'Q2': [2, 3, 1, 2, 3],
                  'Q3': [1, 5, 2, 4, 4]})

print(data)

result = data.apply(pd.value_counts).fillna(0)

print(result)

stringData = Series(['aaa', 'bbbb', np.nan, 'ccccc'])
print(stringData)

print(stringData.isnull())

stringData[0] = None

print(stringData.isnull())

print(stringData)
