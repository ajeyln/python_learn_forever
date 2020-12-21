# Assigning name to series's index
import pandas as  pd

ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz')) # series

ser.name = 'alphabets' # assign the name as "alphabet"
print(ser.head())