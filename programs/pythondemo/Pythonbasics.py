# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:39:57 2020

@author: lenovo
"""
print('Hello.Welcome to python')
num1=100
num2 = 200
num3 = num1+num2
print(num3)
#int age = 100
'''
Datatypes

int
float
str
bool - True/False
'''
age = 45
print(age)
type(age)
amt = 20004.5
print(amt)
print(type(amt))

course = 'I am learning Python'
type(course)

isItRaining = True
print(type(isItRaining))

'''
list
tuple
dictionary
set
'''
#List - Dynamic, Allows duplicates,maintains the order
evennumber =[2,4,6,8]
print(evennumber)
print(type(evennumber))
#<class 'list'>
fruits =[1,'Apple',2,'Grapes',3,'Banana','Banana']
fruits[0]

#Tuple - constant list

days=('Mon','Tue','Wed')

#Dictionary - Key : Value pair,won't allow duplicates,it does not maintain the order 

aadhardict ={"Raghu":9898989898,"Vidya":8978675445}

#Set - won't allow duplicates

numset = {1,3,5,7,9}

'''
Operators 
Arithmetic,Relational,Logical,Bitwise
'''

'''
Arithmetic - +,-,*,/,//,%,**
'''

num1=10
num2 = 15

res = num1 + num2
print('Addition of ',num1, " and ",num2," is ",res)

res = num2/num1
print('/ usage ',res)

res = num2//num1
print('// usage ',res)

res = num2%num1
print('% usage',res)

'''
Relational - >,<,==,>=,<=,!=
'''
res = num1 > num2
print(" usage of > ",res)

num3 = 10
res = (num1 == num3)
print(' == ',res)


res = (num1 != num2)
print(' != ',res)

'''
Logical and ,or, not
'''

num1=100
num2=50
num3 = 80

(num1 > num2) and (num3 >num2)

res = (num1 != num2) or (num3 <num2)
print('usage of or',res)
not (num1 != num2)

'''
Loops - while , for
#1 ...100
'''

'''
prints 1 to 10
'''
start = 1
end = 10
while (start <=end):
    print(start)
    start = start + 1
    
'''
prints 10 to 1
'''
start = 10
end = 1
while (start >=end):
    print(start)
    start = start - 1

'''
for loop
range()
'''

'''
prints 0 to 10
'''
for i in range(11):
    print(i)
    
'''
prints 1 to 10
'''
for i in range(1,11):
    print(i)


'''
prints 2's table
'''
for i in range(2,21,2):
    print(i)

'''
prints 50 to 20 

'''
for i in range(50,19,-2):
    print(i)


'''
print table of any given number
3
6
9
'
'
30
'''

n=2
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    
'''
conditional statements  if,elif,else
''' 

age = 17
if (age >=18):
    print('You are eligible to vote')
else:
    print('you are not eligible to vote')

'''
Given the marks of a student. Find the grade
'''

marks = 82

if (marks >90 and marks <=100):
    print('A+')
elif (marks >80 and marks <=90):
    print('A')
elif (marks >70 and marks <=80):
    print('B+')
else:
    print('Lesser than B+')
    
    
'''

Electricity Bill

upto 100 units 1 rs/unit
Between 101 to 200 units - 2 rs/unit
Between 201 to 300 units - 3 rs/unit
Above 300 units - 4 rs/unit

Based on the meter reading calculate the bill

140

first 100 unit - 1 * 100 - 100
next 40 units - 2 * 40 - 80 
Total - 180
'''

units=250
if (units <= 100): 
    print( units * 1)
  
elif (units <= 200): 
    print(((100 * 1) + (units - 100) * 2)) 
  
elif (units <= 300):      
    print( ((100 * 1) + (100 * 2) + (units - 300) * 3))
  
elif (units > 400): 
  print( ((100 * 1) + (100 * 2) +  (100 * 3) + (units - 400) * 4))

name = input ("Enter your name")
print('your name is ',name)
age = int(input("Enter your age"))
print(age)
amount = float(input("Enter the amount purchased"))
print('you have purchased goods worth ',amount)
#[20,30,399,3939]
friendslst = eval (input("enter your friends"))
print(friendslst)

   
    
























