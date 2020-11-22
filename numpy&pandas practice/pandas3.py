import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data = {"Seoul": 4000, "Busan": 2000, "Incheon": 1500, "Kwangju": 1000}
obj = Series(data)

print(data)
print(obj)

city = ["Seoul", "Daegu", "Incheon", "Kwangju"]
obj2 = Series(data, index=city)

print(obj2)

print(obj+obj2)

obj2.name = "인구수"
print(obj2)

obj2.index.name = "도시"
print(obj2)

obj2.index = ["Daejeon", "Jeju", "Jeonju", "Ulsan"]
print(obj2)

a = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a)

data = {
    'city': ['seoul', 'busan', 'daegu', 'jeju'],
    'year': [2000, 2005, 2010, 2015],
    'population': [4000, 2000, 1000, 1000]
}

df = pd.DataFrame(data)

print(df)

df2 = DataFrame(data, columns=['year', 'city', 'population'])

print(df2)

df3 = DataFrame(data, columns=['year', 'city',
                               'population', 'debt'], index=['one', 'two', 'three', 'four'])
print(df3)

print(df3['city'])
print(df3['year'])

print(df3.columns)
print(df3.index)

df3['debt'] = 1000
print(df3)

df3['debt'] = np.arange(4)

print(df3)

val = Series([1000, 2000, 3000, 4000], index=['one', 'two', 'three', 'four'])

df3['debt'] = val

print(df3)

val1 = Series([1000, 3000, 5000], index=['one', 'three', 'four'])

df3['debt'] = val1
print(df3)

df3['aaa'] = df3.city == 'seoul'
print(df3)

del df3['aaa']
print(df3.columns)


data2 = {'seoul': {2001: 20, 2002: 30},
         'busan': {2000: 10, 2001: 200, 2002: 300}}

df4 = DataFrame(data2)
print(df4)


print(df4.T)

print(df4.values)
