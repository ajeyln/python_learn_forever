# Reshape the series ser into a dataframe with 7 rows and 5 columns

import pandas as pd
import numpy as np
ser = pd.Series(np.random.randint(1, 10, 35))

df = pd.DataFrame(ser.values.reshape(7,5))
print(df)