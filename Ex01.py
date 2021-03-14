# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:27:45 2021

@author: user
"""

for i in range(5,0,-1): #[0,1,2,3,4]
   
    for a in range(0,i):
        print('*',end='')
    print()

for i in range(1,5):
    for a in range(0,i+1):
        print('*',end='')
    print()
    
print("程式執行完畢")