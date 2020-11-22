import pandas as pd
from pandas import Series, DataFrame
pip3 install xlrd

obj = Series([4, 7, -5, 3])
print(obj)

print(obj.values)
print(obj.index)

obj2 = Series([10, 1, 8, 3], index=["x", "y", "z", "w"])

print(obj2)

print(obj2.index)

data = {'state': ['Seoul', 'Busan', 'Daegu'],
        'year': [2000, 2010, 2015]}

Frame = DataFrame(data)

print(Frame)

fileName = "stat.xlsx"
sheet_name = "st"
book = pd.read_excel(fileName, sheetname=sheet_name, header=2)
book = book.sort_values(by="2016", ascending=False)
print(book)
