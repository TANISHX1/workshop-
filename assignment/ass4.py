import pandas as pd
import numpy as np
# Q1
dic = {'Name':['Alice','Bob','Charlie','David','Eca'],
       'Age':[25,30,22,35,28],
       'Grade':[88,75,92,68,90] }

students = pd.DataFrame(dic)
print(students)
print("*"*60)
# -------------------------------------------------

# Q2
# students.drop(labels=3,axis=0,inplace=True)
idx_david = students[students['Name'] == 'David'].index
students.drop(idx_david,inplace=True)
print(students)
print("*"*60)
# -------------------------------------------------

# Q3
print((students[students['Age'] >25])[['Name','Grade']])

print("*"*60)
# -------------------------------------------------

# Q4
students['Grade_squared'] = students['Grade']**2
print(students)
print("*"*60)
# -------------------------------------------------

# Q5
students.sort_values(by='Grade',inplace=True,ascending=False)
print(students)
print("*"*60)
# -------------------------------------------------

# Q6
mean = students['Grade'].mean()
std_deviation = students['Grade'].std()
skew = students['Grade'].skew()
kurt = students['Grade'].kurtosis()
print(f"Mean :{mean}\n Standard Deviation : {std_deviation}")
print(f"Skewness: {skew}\nKurtosis :{kurt}")
print("*"*60)
# -------------------------------------------------

# Q7
values , count = np.unique(students['Age'],return_counts=True)
print(f"Values :{values}")
print(f"Count : {count}")
print("*"*60)
# -------------------------------------------------

# Q8
present = students[students['Name'].isin(['Alice'])]
print(f"Alice is : \n{present}")
print("*"*60)
# -------------------------------------------------

# Q9
students.to_csv('student_data.csv',index_label=False)
print("DOne")
print("*"*60)
# -------------------------------------------------

# Q9
read_students = pd.read_csv('student_data.csv')
print(read_students)