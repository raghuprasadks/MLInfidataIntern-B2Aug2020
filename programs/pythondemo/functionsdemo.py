# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:04:25 2020

@author: lenovo
"""


def greet():
    print('Welcome to Python')
    
print('out side of the function')

greet()

def greet(name):
    print(name, ' welcome to python')

greet('ravi')


def add(n1,n2):
    return n1+n2
    
total = add(10,20)
print('total is ',total)


def si(p,r,t):
    sical = p*r*t/100
    return sical,p,r,t

simpleinterest,p,r,t = si(1000,6,1)
print('Simple interest P : ',p,' ROI ',r, 'time ',t, ' is ', simpleinterest)


def multiargs(* args):
    print('multiple args',args)
    
multiargs(1,2,3)
multiargs(10,20,30,40,50,60)

def keywords(** kwrds):
    print (kwrds)
    
keywords(name='raghu',age=45,city='Bengaluru')


def fact(n):
    if n==0:
        return 1 
    else:
        return n*fac(n-1)

n=int(input("enter no:"))
print(fact(n))




    
