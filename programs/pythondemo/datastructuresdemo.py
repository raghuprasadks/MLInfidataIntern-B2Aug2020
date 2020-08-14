# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:53:22 2020

@author: lenovo
"""

'''
List
'''

data=[2,4,6,8]
print(data)
# Adding element to a list
data.append(10)
lst=[3,5,7,9]
newlist = data+lst
print(newlist)

#update an element
data[0] = 20

#listing
for i in newlist:
    print(i)
    
del data[1]

print('after delete ',data)

#Remove specific value
data.remove(8)

print('length of a list ',len(data))

print('new list',newlist)

print('maximum ',max(newlist))
print('minimum ',min(newlist))
print('sum ',sum(newlist))
print('average',sum(newlist)/len(newlist))

#slicing
print('new list',newlist)
print('slicing ' ,newlist[0:4])
anotherlist = newlist[4:9]
print('after slicing ',anotherlist)

lst=[4,7,1,78,46,300,57]

interns =[]
header=['name','college','branch','mobile']
interns.append(header)

stud1 = ['Trishakthi','BMSIT','EC',7349416512]
interns.append(stud1)

'''
dictionary
Key : value
'''

telelist = {'raghu':748787878,'ramesh':9393939,'gagana':939393}
print(telelist)
print(type(telelist))
print('mobile of raghu ',telelist['raghu'])
telelist = {'raghu':748787878,'ramesh':9393939,'gagana':939393,'ramesh':9393938}
telelist['ramesh']
len(telelist)


print('keys ',telelist.keys())
print('values ',telelist.values())

for k,v in telelist.items():
    print('key ',k, ' value ',v)

telelist.update({'raghu':9845547471})
print('updated list',telelist)

del telelist['ramesh']

'''
Create a list from scratch
List of employee - code:name
'''

noemp = int(input('Enter number of employees'))

empdict = {}
for i in range(noemp):
    code= int(input("enter code"))
    name= input("enter name")
    empdict[code]=name
print('emp list ',empdict)

'''
Tuple - Constant list
'''

days=('Mon','Tue','Wed','Thu')
print(days)
print(type(days))

'''
cannot append
cannot modify
'''
days.append('Fri')

days[1]='Tuesday'

del days[0]

daysubset = days[0:3]
print(daysubset)

print(len(days))

test = 100,200,300
type(test)

#Packing and unpacking
p,q,r =test
print(p,q,r)


'''
set - does not duplicate value
Organizes data in ascending order
'''

set1 = {2,4,6,4,8,10}
print(set1)

set1.update({19,4,20,8})

print(set1)


data = [1,4,2,6,9,8]
data.sort()
print('sorting in ascending order',data)

data.sort(reverse = True)
print('sorting in desending order',data)








