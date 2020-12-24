# creating a column that contains the penultimate value in each row.
# (Create a new column 'penultimate' which has the second largest value of each row of df.)

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

out = df.apply(lambda x: x.sort_values().unique()[-2], axis=1)
df['penultimate'] = out
print(df)