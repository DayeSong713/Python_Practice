'''중복색인'''

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])

print(obj)

print(obj['a'])

print(obj['c'])

print(obj['b'])

df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])

print(df)
