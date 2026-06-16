import pandas as pd
import numpy as np
data = {'Name':['Priya','Vishnu','Rajesh',' Anitha','Murugan'],
        'Age':[24,27,35,30,29],
        'Salary':[50000,60000,35000,55000,45000],
        'Department':['IT','HR','MANAGER','TL','HR']}
df = pd.DataFrame(data)
print("Employee Data:")
print(df)
print(f"\nShape:{df.shape}")

print("----------------------------")
df_rename = df[['Name', 'Age', 'Salary', 'Department']].copy()
print("Original columns:")
print(df_rename.columns.tolist())
print("\nOriginal DataFrame:")
print(df_rename)
print("----------------------------")
df_rename.rename(columns={
    'Name': 'Employee_Name',
    'Salary': 'Annual_Salary',
    'Department': 'Dept'},inplace=True)

print("\nAfter renaming:")
print(df_rename.columns.tolist())
print("\nRenamed DataFrame:")
print(df_rename)

print("----------------------------")
df[['Name', 'Age', 'Salary', 'Department']].to_csv('employees.csv', index=False)
print("Data saved to 'employees.csv'")
print("\nFirst few lines of CSV file:")
with open('employees.csv', 'r') as file:
    print(file.read())


print("----------------------------")
print("Data types in our DataFrame:")
print(df[['Name', 'Age', 'Salary']].dtypes)

print("----------------------------")
df['Age_int'] = df['Age'].astype(int)
print("\nAfter converting age to intger:")
print(f"original age type:{df['Age'].dtype}")
print(f"new age_int type:{df['Age_int'].dtype}")

print("----------------------------")
df['Salary_str'] = df['Salary'].astype(str)
print("Salary as string:")
print(df['Salary_str'])
print(f"Type:{df['Salary_str'].dtype}")

print("----------------------------")
df_str = pd.DataFrame({
    'Name': ['Priya Dharshini', 'Vishnu Prasad', 'Rajesh Kannan'],
    'Email': ['priya@company.com', 'vishnu@company.com', 'rajesh@company.com']})

print("Original DataFrame:")
print(df_str)

print("----------------------------")
print("\nNames in UPPERCASE:")
print(df_str['Name'].str.upper())

print("----------------------------")
print("Names in lowercase:")
print(df_str['Name'].str.lower())


print("----------------------------")
print("\nLength of each name:")
print(df_str['Name'].str.len())

print("----------------------------")
print("First names only:")
df_str['FirstName'] = df_str['Name'].str.split(' ').str[0]
print(df_str)

df_str['LastName'] = df_str['Name'].str.split(' ').str[1]
print("\nWith Last Name:")
print(df_str)

print("----------------------------")
employees = pd.DataFrame({
    'Employees ID': [1, 2, 3, 4, 5],
    'Name': ['Priya', 'Vishnu', 'Rajesh', 'Anitha', 'Murugan'],
    'Department': ['IT', 'HR', 'MANAGER', 'TL', 'HR']
})

salaries = pd.DataFrame({
    'Employees ID': [1, 2, 3, 4, 5],
    'Salary': [50000, 60000, 35000, 55000, 45000]
})

print("Employees DataFrame:")
print(employees)
print("\nSalaries DataFrame:")
print(salaries)

print("----------------------------")
merged_df = pd.merge(employees, salaries, on='Employees ID')
print("After merging on EmpID:")
print(merged_df)

print("----------------------------")





