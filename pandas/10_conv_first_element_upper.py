# Change the first character of each word to upper case in each word of ser.

import pandas as pd 

ser = pd.Series(['how', 'to', 'kick', 'football'])

print(ser.map(lambda x: x.title()))