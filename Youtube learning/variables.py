# -*- coding: utf-8 -*-
"""
LINKS:
 --- video tutorial -----
* https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=1s

* the new boston is also a great youtube channel

* https://www.geeksforgeeks.org
this descrips methods perfectly


"""


'''
defining variables
'''


"""
name = 'John Smith'
age = 20
is_newPatient = True
"""

#input (ask the user to enter a content)
"""
userName = input('what is your name? ')
userColor = input('what is your favorite color? ')
print(userName +' likes ' + userColor)
"""

#calculate age 
"""
birth_year =int(input('Birth year ? '))
age = 2019 - birth_year
print('your age is : ' + str(age)) 
"""

#Convert pound to Kilograms
""" 
user_pounds = input('Enter your weight in pounds : ')
conversionFactor = 0.453
calculated_weigt = float(user_pounds) * conversionFactor
print('your weight in KG is : '+str(calculated_weigt))
"""
#Strings
"""
course = "Pythos's course for  beginners" # showing 's signal
couser = 'Python for "beginners"' # showing "" signal
longString = '''Hi jones
I want to thank you
for coming today'''
#print(couser + ' ****** ' + course)
print(longString)
#print(longString[0])# showing first character 
#print(longString[-1])#showing last character
print(longString[0:3])#showing last character
"""

#Formatted Strings
"""
first = 'John'
last = 'Smith'
message = first + ' ['+ last + '] is a coder'
#showing it with Formatted Strings
msg = f'{first} [{last}] is a coder WOW'
print(message)
print(msg)
"""
#String Methods
#length - upper -lower - find - replace - in - 
"""
message = 'python FOR Beginners'
print(message.capitalize()) # first letter is uppercase and rest all small
print(message.title())# each first letter in all words will be uppercase
print(message.upper())
print(message.lower())
print(len(message))
print(message.find('for'))
print(message.replace('Beginners','Absolut beginners'))
string = "geeks for geeks geeks geeks geeks" 
print(string.replace('geeks','weeks')) 
print(string.replace('geeks','weeks',3)) #3 is how many times to replace 
print('geeks' in string) # checking if this phrase in a variable and 
# return a bool value
"""

Arithmetic Operations

