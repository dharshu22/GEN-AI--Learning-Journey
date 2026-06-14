import pandas as pd
Places  = pd.Series(['Kodaikanal','Ooty','Yercaud','Kolli Hills'])
print('Series of Places:')
print(Places)

prices = pd.Series([3000,4000,1000,2000], index=['Kodaikanal','Ooty','Yercaud','Kolli Hills'])
print('Places prices:')
print(prices)

Things = pd.Series(['chair','table','photo','waterbottle'],
                index=['wooden','wooden','glass','plastic'])
print(Things)
print('only wooden Things:',Things['wooden'])

studentname_rollnumber = pd.Series({'Priya':12,'Sachin':13,'Vishnu':14,'Anitha':15})
print("studentname roll number:")
print(studentname_rollnumber)

print("\nSET OF ROW FROM START")
studentname_rollnumber = pd.Series({'Priya':12,'Sachin':13,'Vishnu':14,'Anitha':15})
print("studentname rollnumber:")
print(studentname_rollnumber.head(3))

print("\nSET OF ROW FROM END")
studentname_rollnumber = pd.Series({'Priya':12,'Sachin':13,'Vishnu':14,'Anitha':15})
print("studentname rollnumber:")
print(studentname_rollnumber.tail(3))



