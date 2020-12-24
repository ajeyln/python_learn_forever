# From ser, extract words that contain atleast 2 vowels.
import pandas as pd
from collections import Counter

ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money','Ajeya','Brown'])

mask = ser.map(lambda x: sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
print(ser[mask])