# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:08:29 2020

@author: lenovo
"""

'''
1. Establish connection with database
'''
import sqlite3

conn = sqlite3.connect("test.db")
print('Connection successful')

'''
2. Create a table
'''

conn.execute('''
                create table customer(
                code int primary key NOT NULL,
                name text NOT NULL,
                email text NOT NULL,
                mobile int NOT NULL,
                address text NOT NULL,
                pincode int)              
              ''')

print('customer table is created')

'''
3. Insert data
'''

conn.execute('''
             insert into customer values(1,"raghu","prasadraghuks@gmail.com",9845547471,'Indushankara,23 Cross,Jakkuru,Bengaluru',560077)     
             ''')
conn.execute('''
             insert into customer values(2,"ramya","ramya@gmail.com",9845547472,'Indushankara,23 Cross,Jakkuru,Bengaluru',560077)     
             ''')


conn.commit()
print('Record inserted to customer table')
#conn.close()

'''
4. Select Data
'''

records = conn.execute('select code,name,email,mobile,address,pincode from customer')

for record in records:
    
    print("code = ",record[0])
    print("name = ",record[1])
    print("email = ",record[2])
    print("mobile = ",record[3])
    print("address = ",record[4])
    print("pincode = ",record[5])
    
print('Records extracted successfully')
conn.close()
    
    
'''
5. Update Data
'''

conn.execute("update customer set name='raghu prasad' where code=1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)


'''
6. Delete Data
'''

conn.execute("delete from customer where code=1")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

conn.close()    
    
    
    
    






