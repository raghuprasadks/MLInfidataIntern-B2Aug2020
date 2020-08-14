# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:44:25 2020

@author: lenovo
"""

'''

Object Oriented Programming

Proper and functionality


TVRemote

- Physical properties - shape,size,color,buttons

- functionality - swic on ,swit - off, volume,mode,channel

class - blueprint 
instance - object

mould - blue print
object - ganesha raghu's'

civil construction -
apartment

plan - blueprint
Block A - 100
B - 200
object 

Relate
Reusability
Module
'''


class Student():
    code=0
    name=''
    college=''
    branch=''
    sem=0
    
    def admission(self,code,name,college,branch,sem):
        self.code = code
        self.name = name
        self.college = college
        self.branch = branch
        self.sem = sem
    
    def info(self):
        
        return 'Code ',self.code,' Name : ',self.name ,' College :',self.college        
        
ramya = Student()
ramya.admission("1","Ramya ","MSRIT","CS",5)
print('Info :Ramya ',ramya.info())
        

narayan = Student()
narayan.admission("2","Narayan ","PES","CS",7)
print('Info :narayan ',narayan.info())
        
import random

class Account():
    
    def openAccount(self,name,email,mobile,address,idproof):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address
        self.idproof = idproof
        self.accountno = random.randint(100, 1000)
        self.balance = 0
        return self.accountno        
        
    def deposit(self,acctno,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self,acctno,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def checkBalance (self,acctno):
        return self.balance
        
raghu = Account()
actno = raghu.openAccount("Raghu Prasad", 'prasadraghuks@gmail.com', 9845547471, "Jakkuru,Benaluru", 9939393939)
print('Account No ',actno)        
bal = raghu.deposit(actno,10000)
print('Balance after deposit of 10 k',bal)
bal = raghu.deposit(actno,15000)
print('Balance after deposit of 15 k',bal)
bal = raghu.withdraw(actno,3000)
print('Balance after withdraw of 3 k',bal)
bal = raghu.checkBalance(actno)
print('Check Balance',bal)

'''
Constructor 
'''

import random

class Account():
    '''
    Constructor
    
    Account()
    Account()
    '''
    def __init__(self,name,email,mobile,address,idproof):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address
        self.idproof = idproof
        self.accountno = random.randint(100, 1000)
        self.balance = 0
        #return self.accountno        
        
    def deposit(self,acctno,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self,acctno,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def checkBalance (self,acctno):
        return self.balance
        
ravi = Account("Ravi Prasad", 'prasadraviks@gmail.com', 9845547472, "Vijaya Nagara,Benaluru", 9939393940)
#actno = raghu.openAccount("Raghu Prasad", 'prasadraghuks@gmail.com', 9845547471, "Jakkuru,Benaluru", 9939393939)
actno = ravi.accountno
print('Account No ',actno)        
bal = ravi.deposit(actno,12000)
print('Balance after deposit of 12 k',bal)
bal = ravi.deposit(actno,15000)
print('Balance after deposit of 15 k',bal)
bal = ravi.withdraw(actno,3000)
print('Balance after withdraw of 3 k',bal)
bal = ravi.checkBalance(actno)
print('Check Balance',bal)

'''
108 Dosas - Batter,chetney,ghee,Masala,Corn,Cheese
'''


class Student():
    
    def __init__(self,code,name,sub1,sub2,sub3,total):
        self.code = code
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.total = total         
          
    def info(self):        
        return 'Code ',self.code,' Name : ',self.name ,' Sub1 :',self.sub1, ' Sub 2',self.sub2,'Sub3 ',self.sub3,' total ',self.total      


studentList = []
raghu = Student(1,'raghu',90,80,70,230)
#print(raghu.info())
studentList.append(raghu)

ravi = Student(2,'ravi',80,90,90,260)
#print(ravi.info())
studentList.append(ravi)

ambika = Student(3,'ambika',70,65,95,240)
#print(ambika.info())
studentList.append(ambika)


topper = 0
sub1topper = 0

for i in studentList:
    #print(i.info())
    if(i.total > topper):
        topper=i.total
        
    if(i.sub1 > sub1topper):
        sub1topper=i.sub1
        
print('topper marks is ',topper)
print('sub1topper marks is ',sub1topper)

'''
Topper details
'''
topper = 0
indextopper = 0

for i in range(len(studentList)):
    stud = studentList[i]
    #print(i.info())
    if(stud.total > topper):
        topper=stud.total
        indextopper=i
        
print('topper info',studentList[indextopper].info())
    
'''
dictionary 
'''    
    
studentDict = {}
raghu = Student(1,'raghu',90,80,70,230)
#print(raghu.info())
#studentList.append(raghu)
studentDict["stud1"]=raghu

ravi = Student(2,'ravi',80,90,90,260)
#print(ravi.info())
#studentList.append(ravi)
studentDict["stud2"]=ravi

ambika = Student(3,'ambika',70,65,95,240)
#print(ambika.info())
#studentList.append(ambika)

studentDict["stud3"]=ambika

print('Student Dictionary ',studentDict)

for k,v in studentDict.items():
    print("Key ",k)
    print("Value ",v.info())












    

    
    
    
        
        
        
        
        
        
        
    
    
    
