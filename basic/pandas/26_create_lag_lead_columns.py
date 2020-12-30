# create lags and leads of a column in a dataframe
# Create two new columns in df, one of which is a lag1 (shift column a down by 1 row) of column ‘a’ and the other is a lead1 (shift column b up by 1 row).

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns = list('abcd'))
print("DataFrame before adding the columns\n")
print(df)

print("\n DataFrame before adding the columns")

df['a_lag1'] = df['a'].shift(1)
df['b_lead1'] = df['b'].shift(-1)
print(df)