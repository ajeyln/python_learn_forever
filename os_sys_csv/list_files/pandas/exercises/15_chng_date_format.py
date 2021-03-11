# Change ser to dates that start with 4th of the respective months.

import pandas as pd
from dateutil.parser import parse

# Input
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])

# Parse the date
ser_ts = ser.map(lambda x: parse(x))

# Construct date string with date as 4
ser_datestr = ser_ts.dt.year.astype('str') + '-' + ser_ts.dt.month.astype('str') + '-' + '04'

# Format it.
[parse(i).strftime('%Y-%m-%d') for i in ser_datestr]
print(ser.map(lambda x: parse('04 ' + x)))