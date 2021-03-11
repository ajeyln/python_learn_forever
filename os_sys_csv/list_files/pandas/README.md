<h1 align="Center"> Pandas Module</h1>

### What is **Pandas Modules** in Python ? <br>
   + Pandas is used for data manipulation, analysis and cleaning. <br>
   + Pandas is an open source library in Python. It provides ready to use high-performance data structures and data analysis tools. <br>
   + Pandas module runs on top of NumPy and it is popularly used for data science and data analytics.

### what are **Dataframes** and **Series** ? <br>
   + DataFrame is the key data structure in Pandas. It allows us to store and manipulate tabular data as a 2-D data structure. <br>
   + Pandas provides a rich feature-set on the DataFrame. For example, data alignment, data statistics, slicing, grouping, merging, concatenating data, etc.

### What are the **Data Structure** in  Pandas Module ? <br>
 
There are 3 data structures provided by the Pandas module <br>
	**Series**: It is a 1-D size-immutable array like structure having homogeneous data. <br>
	**DataFrames**: It is a 2-D size-mutable tabular structure with heterogeneously typed columns. <br>
	**Panel**: It is a 3-D, size-mutable array

### What are **DataFrames** ?

   + DataFrame is the most important and widely used data structure and is a standard way to store data.<br>
   + DataFrame has data aligned in rows and columns like the SQL table or a spreadsheet database. <br>

We can either create a code into a DataFrame or import a CSV file, tsv file, Excel file, SQL table, etc.

#### We can use the below constructor for creating a DataFrame object.<br>
**pandas.DataFrame(data, index, columns, dtype, copy)** <br>

 Where <br>
**data** – create a DataFrame object from the input data. It can be list, dict, series, Numpy ndarrays or even, any other DataFrame. <br>
**index** – has the row labels <br>
**columns** – used to create column labels <br>
**dtype** – used to specify the data type of each column, optional parameter <br>
**copy** – used for copying data

Eg: Simple code to create a Dataframe from the list of dictionaries  <br>

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "State": ['Andhra Pradesh', 'Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu'],
    "Capital": ['Hyderabad', 'Mumbai', 'Bengaluru', 'Trivandrum', 'Chennai'], 
    "Literacy %": [89, 77, 82, 97,85],
    "Avg High Temp(c)": [33, 30, 29, 31, 32 ]
})
print(df) 
```

It will show the output as  <br>
| | State | Capital| Literacy %	| Avg.High Temp(C) |
|----|------|---------|-------|-------------|
|0|  Andhra Pradesh|	Hyderabad|	89	|	33 |
|1|	Maharastra|		Mumbai|			77		|	30 |
|2|	Karnataka|		Bengaluru|		82		|	29 |
|3|	Kerala|			Trivandrum|		97		|	31 |
|4|	Tamil Nadu|		Chennai|		85	|   32 |
### How to select the dats in DataFrame ?

Pandas provide many useful functions to inspect only the data we need. <br>
We can use **df.head(n)** to get the first n rows and **df.tail(n)** to print the last n rows. <br>
For example, the below code prints the first 2 rows and last 1 row from the DataFrame.

```python
print(df.head(2))
```

Output will show first 2 rows in Dataframes  <br>
| | State | Capital| Literacy %	| Avg.High Temp(C) |
|----|------|---------|-------|-------------|
|0|  Andhra Pradesh|	Hyderabad|	89	|	33 |
|1|	Maharastra|		Mumbai|			77		|	30 |


```python
print(df.tail(3))
```

Output will show last 3 rows in Dataframes  <br>
| | State | Capital| Literacy %	| Avg.High Temp(C) |
|----|------|---------|-------|-------------|
|2|	Karnataka|		Bengaluru|		82		|	29 |
|3|	Kerala|			Trivandrum|		97		|	31 |
|4|	Tamil Nadu|		Chennai|		85	|   32 |

### How to filter the data ?

It is also possible to filter on column values (Any comparison operator can be used to filter, based on a condition). <br>

For example, below code filters the columns having Literacy% above 90%.<br>

```python
print(df[df['Literacy %']>90])
```

It will show the output as  <br>
| | State | Capital| Literacy %	| Avg.High Temp(C) |
|----|------|---------|-------|-------------|
|3|	Kerala|			Trivandrum|		97		|	31 |

Another way to filter data is using the **isin**. <br>
Following is the code to filter only 2 states ‘Karnataka’ and ‘Tamil Nadu’.

```python
print(df[df['State'].isin(['Karnataka', 'Tamil Nadu'])])
```

It will show the output as  <br>
| | State | Capital| Literacy %	| Avg.High Temp(C) |
|----|------|---------|-------|-------------|
|2|	Karnataka|		Bengaluru|		82		|	29 |
|4|	Tamil Nadu|		Chennai|		85	|   32 |

### How to rename column ?

It is possible to use the **df.rename()** function to rename a column and the function takes the old column name and new column name as arguments. <br>

For example, we can rename the column ‘Literacy %’ to ‘Literacy percentage’.


```python
df.rename(columns = {'Literacy %':'Literacy percentage'}, inplace=True) 
print(df.head())
```

The argument `inplace=True` makes the changes to the DataFrame.

It will show the output as  <br>
| | State | Capital| Literacy percentage	| Avg.High Temp(C) |
|----|------|---------|-------|-------------|
|0|  Andhra Pradesh|	Hyderabad|	89	|	33 |
|1|	Maharastra|		Mumbai|			77		|	30 |
|2|	Karnataka|		Bengaluru|		82		|	29 |
|3|	Kerala|			Trivandrum|		97		|	31 |
|4|	Tamil Nadu|		Chennai|		85	|   32 |