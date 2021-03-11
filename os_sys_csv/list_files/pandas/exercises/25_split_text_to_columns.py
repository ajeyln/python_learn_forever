# Split the string column in df to form a dataframe with 3 columns as shown.

import pandas as pd
import numpy as np

df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])
print(df )
print("\n Spliting the text in first column into 2 columns \n")
df_out = df.row.str.split(',|\t', expand=True )

new_header = df_out.iloc[0] # Make first row as header
df_out = df_out[1:]
df_out.columns = new_header
print(df_out)