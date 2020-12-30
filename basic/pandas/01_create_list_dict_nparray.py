# A simple program to create a Series of dictionaries using list,Numpy array and pandas
import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))


ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)
print(ser1.head())