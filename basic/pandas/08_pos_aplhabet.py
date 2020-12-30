# From ser, extract the items at positions in list pos.
import pandas as pd
import numpy as np

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

print(ser.take(pos))