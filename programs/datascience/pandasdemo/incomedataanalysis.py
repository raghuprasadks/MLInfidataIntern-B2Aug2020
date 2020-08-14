# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:23:16 2020

@author: lenovo

Analysis of income data using pandas
"""

import pandas as pd

income = pd.read_csv("income.csv")

print('income data')
print(income)
print('data type ',type(income))
'''
<class 'pandas.core.frame.DataFrame'>
'''
print('data size ',income.shape)
row=income.shape[0]
print('rows ',row)

columns=income.shape[1]
print('column size ',row)

print('Columns : ')
print(income.columns)

print('column state ',income.columns[1])
print('0 and 1st column ',income.columns[0:2])

print('Data types of income df')
print(income.dtypes)
print('data type of State field')
print(income['State'].dtypes)
print('data type alternatively ',income.State.dtypes)
income.Y2008 = income.Y2008.astype(float)
print(income.dtypes)
print('first five records from the top')
print(income.head())
income5 =income.head()

print('last five records from the bottom')
print(income.tail())

income.head(2)  #shows first 2 rows.

income.tail(2)  #shows last 2 rows.



'''
Extract records 5 to 10
'''
income[5:10]
income.iloc[5:10]

'''
Category
'''
s = pd.Series([1,2,3,1,2], dtype="category")
print(s)

print('Unique values in Index column')
print(income.Index.unique())

print('Number of unique values')
print(income.Index.nunique())
print('Cross tab')
print(pd.crosstab(income.Index,income.State))

print('Value count ')
income.Index.value_counts()
income.Index.value_counts(ascending=True)

income.loc[:,["Index","State","Y2008"]]

income.loc[[1,2],["Index","State","Y2008"]]

income.iloc[:,0:5]

import numpy as np
np.arange(1,20,2)

x = pd.DataFrame({"var1" : np.arange(1,20,2)}, index=[9,8,7,6,10, 1, 2, 3, 4, 5])
print(x)
x.loc[[1,2],:]
x.iloc[[1,2],:]

data = pd.DataFrame({"A" : ["John","Mary","Julia","Kenny","Henry"], "B" : ["Libra","Capricorn","Aries","Scorpio","Aquarius"]})
print(data) 

data.columns = ['Names','Zodiac Signs']
print(data)

#data.rename(columns = {"Names":"Cust_Name"},inplace = True) 
newdata = data.rename(columns = {"Names":"Cust_Name"}) 
print('new data ',newdata)
print('original data ',data)

data.rename(columns = {"Names":"Cust_Name"},inplace = True)
print('original dataset column is changed' ,data)

income.set_index("Index",inplace = True)
index.head()
#Note that the indices have changed and Index column is now no more a column
income.columns
income.reset_index(inplace = True)
income.head()

income.shape
income["difference"] = income.Y2008-income.Y2009
income.shape

income.difference

income["ratio"] = income.Y2008/income.Y2009

income.describe()

income.mean()
income.median()
income.agg(["mean","median"])

income.loc[:,["Y2002","Y2008"]].max()

income.groupby("Index").min()
income.groupby("Index")["Y2002","Y2008"].min()

income.groupby("Index")["Y2002","Y2003"].agg(["min","max","mean"])

income.groupby("Index").agg({"Y2002" : [("Y2002_min","min"),("Y2002_max","max")],
                             "Y2003" : [("Y2003_mean","mean")]})

income[income.Index == "A"]

income[income.Index=="A"]

income.loc[income.Index == "A",:]

income.loc[income.Index == "A","State"]


income.loc[income.Index == "A",:].State

import numpy as np
mydata = {'Crop': ['Rice', 'Wheat', 'Barley', 'Maize'],
        'Yield': [1010, 1025.2, 1404.2, 1251.7],
        'cost' : [102, np.nan, 20, 68]}
crops = pd.DataFrame(mydata)
crops

crops.isnull() 
crops.notnull()
crops.isnull().sum() 

crops.cost.isnull()
crops.dropna()

crops['cost'].fillna(value = "UNKNOWN",inplace = True)
crops

data = pd.DataFrame({"Items" : ["TV","Washing Machine","Mobile","TV","TV","Washing Machine"], "Price" : [10000,50000,20000,10000,10000,40000]})
data
data.duplicated()
data.loc[data.duplicated(),:]

data.loc[data.duplicated(keep = "last"),:] #last entries are not there,indices have changed.

data.drop_duplicates(keep = "first")





