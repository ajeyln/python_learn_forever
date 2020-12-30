# calculating the number of characters in each word in a series

import pandas as pd
ser = pd.Series(['how', 'to', 'kick', 'football?'])

print(ser.map(lambda x: len(x)))