# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:56:57 2020

@author: lenovo
Refer to cheat Sheet on Numpy
"""

import numpy as np

a = np.array([1,2,3])
print('1 d array ',a)

b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
print('2 d array ',b)

c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],
dtype = float)
print('3 d array ',c)

zeros = np.zeros((3,4))
print("zero's array")
print(zeros)

ones = np.ones((2,3,4),dtype=np.int16)
print("one's array")
print(ones)

d = np.arange(10,25,5)
print("Generation of numbers")
print(d)

l = np.linspace(0,2,9)
print("Generation of nine equal distance numbers")
print(l)

e = np.full((2,2),7)
print('constant array')
print(e)


f = np.eye(2)
print('Identify number')
print(f)

r =np.random.random((2,2))
print('random array')
print(r)

e = np.empty((3,2))
print('Empty array')
print(e)

np.save('my_array', a)
np.savez('array.npz', a, b)

l = np.load('my_array.npy')
print('load :: ',l)

np.savetxt("myarray.txt", a, delimiter=" ")

afterload = np.loadtxt("myarray.txt")


g = np.genfromtxt("my_file.csv", delimiter=',')

print('generated number ',g)














