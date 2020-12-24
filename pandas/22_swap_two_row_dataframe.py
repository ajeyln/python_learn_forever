# Swaping two rows in dataframe

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(25).reshape(5, -1))
print(df)

print("\n Swapping 2 rows (1 & 2) in dataframe")
def swap_rows(df, i1, i2):
    a, b = df.iloc[i1, :].copy(), df.iloc[i2, :].copy()
    df.iloc[i1, :], df.iloc[i2, :] = b, a
    return df

print(swap_rows(df, 1, 2))