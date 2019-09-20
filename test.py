# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 'Hello'

print(a.lower())

mydict ={'city':'GBG','name':'Mouhammad','age':'35'}
for key in mydict.keys():
    print (key, '=', mydict[key])
    
    a=list(range(10))
    print(a)
    
    
    for i in a:
        if i>2 :
            print(i)
            
            print('\n\n')
            
while(len(a)>5):
    print(a.pop())
    
    

def double(x):
    """
    some help
    """
    return 2*x



a = list(range(10))
a.reverse()
a = list(zip(a,range(10)))


def getDFirstElement(x):
    return x[0]