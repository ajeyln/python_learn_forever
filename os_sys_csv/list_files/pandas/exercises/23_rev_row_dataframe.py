# Reversing the rows of a dataframe

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(25).reshape(5, -1))
print(df)

print("\n Reversing the rows in dataframe")
print(df.loc[df.index[::-1], :])