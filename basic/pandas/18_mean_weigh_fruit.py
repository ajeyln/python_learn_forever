# Calculating mean weight of fruit

import pandas as pd
import numpy as np

fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))

print(weights.groupby(fruit).mean())