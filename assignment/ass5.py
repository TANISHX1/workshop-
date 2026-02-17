import pandas as pd
import numpy as np

df = pd.read_csv('/home/blazex/Documents/mits/2year/sem4/data_science/pandas/student_data.csv',header=0)
# method 1
mis = df.fillna(0)
print(mis)
# method 2
mis = df.fillna(method='ffill')
print(mis)
# method 3
mis = df.fillna(method='bfill')
print(mis)

# -----------------------------------
# Q2
print("*"*60)
#  we remove duplicate rows for the data (during data cleaning) because :
# 1. to ensure data accuracy and quality
# 2. to prevent from misleading data analyses and statitics
# 3. to maintain the unique identifiers
#  duplicate rows can leads to inaccurate analyses .
#  to identify duplicate rows
dff = df[df.duplicated(keep=False)]
# df.duplicated : it returns a boolean series (if there is duplicated rows then true ,else false)
print('Duplicated : \n ',dff)
#  to remove duplicate 
print(df.drop_duplicates(inplace=True))
# df.drop_duplicates returns the dataframes without duplicate rows
# in above code we are removing the duplicate rows inplace (inplace=true)
print("*"*60)
# ----------------------------------------------
# Q3
def year_f (data_f):
 
    temp_dob = data_f['DoB']
    year  = temp_dob.str[:4]
    return year

data = ({'Name': ['tanish','yash','shruti'],
         'Age' :[20,20,21],
         'DoB' :['2005-08-19','2005-05-16','2005-12-5']})
data_f = pd.DataFrame(data)
print("Orignal Data \n",data_f)
data_f['Year'] = year_f(data_f)
print("Added Year Column :\n",data_f)
# First , create a dataframe
# second , passing the data_f to custom function (year_f) to extract year 
# in year_f , a temp array (temp_dob ) is create with data_f['DoB'] year is extracted through slicing
#  and temp_dob is returned and asigned  to  data_f['Year']
# then , result display / output
print("*"*60)
# ----------------------------------------------
# Q4
data = pd.DataFrame({'A':[1,2,0,5,0,3],
                     'B':[1,0,2,3,0,4],
                     'C':[2,0,7,0,1,0],
                     'D':[2,0,5,8,0,1]})
mean_data = data.replace(0,np.nan).mean()
print(f"Original data :{data}")
print()
print("Mean :",mean_data)
data.replace(0,mean_data,inplace=True)
print()
print(data)
# to replace elements in pandas (in dataframe or in specific column ) with desired value , we use data.replace(value to replace ,value )
# first preparing the dataframe (pd.dataframe())
# replacing the 0 with N/A values to cal. mean without 0 
# calculating the mean ,column-wise (by deafult,axis=0 )
# then replacing all the instance of 0 with the particular column mean value.
# and inplace flag insures modifing the data directly. 
print("*"*60)
# ----------------------------------------------
# Q5 
# using real data 
df = pd.DataFrame(np.random.randint(0,10,size=(5,4)),columns=['A','B','C','D'])
print(f"Original:\n{df}")
standard_d = df.std()
mean_d = df.mean()

lower = mean_d -2*standard_d
upper = mean_d +2*standard_d

print(f"\nlower :\n{lower}\nupper: {upper}\n")
outlier = df[(df<lower) | (df >upper )]
filters = df[(df >=lower) & (df <=upper)]
print(f"Outliers : \n {outlier}")
print(f"filters : \n {filters}")
# Outliers : outliers are the extreme points that differ significently from the dataset
# and lying on abnormal distance from the other points , this are more commonly measurement errors or exponential erros
# identification : generally or more commonly it is identified visually (through scatter plot  , box plot ).
# and statically with the help of interquartile range (IQR) (beyond Q -1.5IQR or 3Q - 1.5IQR) 
# Demonstration 
# first , created a dataframe df
#second, calculated standard devation(standard_d) and mean )mean_d
# calculated lower and upper bound 
# finding the outliers and filters seperately 

# using z-score 
df = pd.DataFrame(np.random.randint(0,100,10))
mean = df.mean()
std = df.std()

df['z-score'] = (df - mean)/std
print()
print(f"Original :\n {df}")
print()
print(f"Mean:{mean}\nstd:{std}")
print()
filter_ = df[np.abs(df['z-score'])<=2]
print(filter_)