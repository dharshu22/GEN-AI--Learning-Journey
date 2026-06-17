import pandas as pd
import numpy as np
data = { 'Name':['Priya','Vishnu','Rajesh','Anitha','Murugan'],
         'Age':[24,27,35,30,29],
         'Salary':[50000,55000,35000,30000,40000],
         'Department':['IT','HR','MANAGER','TL','HR']}
df = pd.DataFrame(data)
print("Employee Data:")
print(df)
print(f"\nShape:{df.shape}")

print("-------------------------")
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [28, 32]})

df2 = pd.DataFrame({
    'Name': ['Charlie', 'Diana'],
    'Age': [25, 30]})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

print("-------------------------")
df_concat = pd.concat([df1, df2],)
print("\nAfter concatenating:")
print(df_concat)

