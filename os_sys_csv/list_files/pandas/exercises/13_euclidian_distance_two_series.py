# Compute the euclidean distance between series (points) p and q, without using a packaged formula

import pandas as pd
import numpy as np
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Solution 1
print(sum((p - q)**2)**.5)

# Solution2 
print(np.linalg.norm(p-q))