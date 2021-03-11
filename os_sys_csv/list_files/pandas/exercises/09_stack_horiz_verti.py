# Stack ser1 and ser2 vertically and horizontally (to form a dataframe).

import pandas as pd
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

ser1.append(ser2) # Vertical

df = pd.concat([ser1, ser2], axis=1)# Horizontal
print(df)
