# Find the positions where values of two columns match

import pandas as pd
import numpy as np

df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                    'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})
print(df)

print("The position where values of two columns match")
array_match = np.where(df.fruit1 == df.fruit2)
print(array_match)