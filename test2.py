import numpy as np
import pandas as pd

a = {'a': 9, 'd': 7, 'c': 4, 'b': 0}
b = {'c': 1, 'd': 3, 'b': 8, 'a': 2}
c = {'b': 2, 'a': 6, 'c': 3, 'd': 5}
d = {'d': 7, 'b': 1, 'a': 6, 'c': 1}

df = pd.DataFrame([a, b, c, d])
df = pd.DataFrame(np.sort(df.values, axis=0), index=df.index, columns=df.columns)
print(df.sort_index(axis=1, ascending=True))