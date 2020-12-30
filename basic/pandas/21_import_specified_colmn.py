# Importing only specified columns (crim & medv) from a csv file 

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', usecols=['crim', 'medv'])
print(df.head())