# Finding the positions of peaks (values surrounded by smaller values on both sides) in series.

import pandas as pd
import numpy as np

ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3]) # Series

dd = np.diff(np.sign(np.diff(ser)))
peak_locs = np.where(dd == -2)[0] + 1
print(peak_locs)