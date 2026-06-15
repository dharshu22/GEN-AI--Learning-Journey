import pandas as pd
import numpy as np
data = { 'Name': ['Priya', 'vishnu', 'Rajesh', 'Anitha', 'Murugan'],
    'Age': [24, 27, 35, 30, 29],
    'Salary': [50000, 60000, 35000, 550000, 45000],
    'Department': ['IT', 'HR', 'MANAGER', 'TL', 'HR'] }

df = pd.DataFrame(data)
print("Employee Data:")
print(df)
print(f"\nShape: {df.shape}")

print("------------------------")
print("EMPLOYEES SORTED BY AGE(young to old):")
print(df.sort_values('Age'))

print("------------------------")
print("EMPLOYEES SORTED BY AGE(old to young):")
print(df.sort_values('Age',ascending=False))

print("------------------------")
print("Sort by Department,then by Salary(highest first):")
print(df.sort_values(['Department','Salary'],ascending=[True,False]))

print("------------------------")
print("Age Statistics:")
print(f"Average Age: {df['Age'].mean():.2f}")
print(f"Median Age: {df['Age'].median()}") 
print(f"Minimum Age: {df['Age'].min()}")
print(f"Maximum Age: {df['Age'].max()}")
print(f"Standard Deviation: {df['Age'].std():.2f}")
print(f"Sum of all Ages: {df['Age'].sum()}")

print("------------------------")
df['Salary_dollar'] = df['Salary'] / 96
print("\nAfter adding Salary_dollar column:")
print(df[['Name', 'Salary', 'Salary_dollar']])

print("------------------------")
def calculate_bonus(dept):
    if dept == 'IT':
        return 5000
    elif dept == 'HR':
        return 7000
    else:
        return 3000

df['Bonus'] = df['Department'].apply(calculate_bonus)
print("After adding Bonus column:")
print(df[['Name', 'Department', 'Bonus']])

print("------------------------")
print("Average Salary by Department:")
dept_avg_salary = df.groupby('Department')['Salary'].mean()
print(dept_avg_salary)
print("\nType:", type(dept_avg_salary))

print("------------------------")
print("Number of employees per Department:")
dept_count = df.groupby('Department').size()
print(dept_count)


print("------------------------")
print("Salary Statistics by Department:")
dept_stats = df.groupby('Department')['Salary'].agg(['mean', 'min', 'max', 'count'])
print(dept_stats)

print("------------------------")
messy_data = {
    'Name': ['Priya', 'Vishnu', 'Rajesh', 'Anitha', 'Murugan'],
    'Age': [24, np.nan, 35, 30, 29],  
    'Salary': [50000, 60000, np.nan, 55000, 45000],  
    'Department': ['IT', 'HR', 'MANAGER', np.nan, 'HR']
}

df_messy = pd.DataFrame(messy_data)
print("DataFrame with Missing Values:")
print(df_messy)
print("------------------------")
print("\nMissing values count per column:")
print(df_messy.isnull().sum())

print("------------------------")
print("Rows with any missing value:")
print(df_messy[df_messy.isnull().any(axis=1)])

print("------------------------")
print("\nRows without any missing value:")
print(df_messy[df_messy.notnull().all(axis=1)])

print("------------------------")
print("Remove rows with missing values")
df_clean1 = df_messy.dropna()
print(f"Original shape: {df_messy.shape}")
print(f"After dropna(): {df_clean1.shape}")
print("\nCleaned DataFrame:")
print(df_clean1)

print("------------------------")
print("Fill missing values")
df_clean2 = df_messy.copy()
df_clean2['Age'].fillna(df_clean2['Age'].mean(), inplace=True)  
df_clean2['Salary'].fillna(0, inplace=True)  
df_clean2['Department'].fillna('--', inplace=True)
print("\nAfter filling missing values:")
print(df_clean2)

print("------------------------")
print("Forward fill")
df_clean3 = df_messy.copy()
df_clean3.fillna(method='ffill', inplace=True)  
print("\nAfter forward fill:")
print(df_clean3)

print("------------------------")
df_new = df[['Name','Age','Salary','Department']].copy()
print("Original DataFrame:")
print(df_new)
print(f"\nColums:{df_new.columns.tolist()}")

print("------------------------")
df_new['Experience'] = [6, 9, 4, 17, 10]  
print("After adding Experience column:")
print(df_new)


print("------------------------")
print("Original columns:", df_new.columns.tolist())
df_drop1 = df_new.drop('Experience', axis=1)
print("\nAfter dropping Experience column:")
print(df_drop1)
print("Columns:", df_drop1.columns.tolist())

print("------------------------")
df_drop2 = df_new.drop(['Age', 'Experience'], axis=1)
print("After dropping Age and Experience columns:")
print(df_drop2)
print("Columns:", df_drop2.columns.tolist())




























