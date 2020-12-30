# Replacing both the diagonals of dataframe with 0

import pandas as pd
import numpy as np

# Input
df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))
print(df)

print("\nReplacing diagonal with zero")

for i in range(df.shape[0]):
    df.iat[i, i] = 0
    df.iat[df.shape[0]-i-1, i] = 0

print(df)