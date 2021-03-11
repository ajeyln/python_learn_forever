# converting a series of date-strings to a timeseries

import pandas as pd
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

# Solution 1
from dateutil.parser import parse
print(ser.map(lambda x: parse(x)))

# Solution 2
print(pd.to_datetime(ser))