import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame({'a': range(7), 'b': range(7, 0, -1),
                'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                'd': [0, 1, 2, 0, 1, 2, 3]})

print(df)

df2 = df.set_index(['c', 'd'])

print(df.set_index(['c', 'd'], drop=False))

print(df2)

print(df2.reset_index())
