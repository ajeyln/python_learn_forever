# From ser1 remove items present in ser2.
import pandas as pd
ser1 = pd.Series([1, 2, 3, 4, 5]) # series 1
ser2 = pd.Series([4, 5, 6, 7, 8]) # series 2

ser1[~ser1.isin(ser2)] 