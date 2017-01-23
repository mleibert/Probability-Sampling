# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:21:58 2017

@author: michael
"""

def max_two(number1,number2):
	if number1 > number2:
		print(number1)
	else:
		print(number2)

max_two(6111,66)

def max_three(number1,number2,number3):
    if number1 > number2 and number1 > number3:
        print(number1)
    elif number2 > number3:
            print(number2)
    else:
            print(number3)
  
max_three(555,55555,5555)

for c in "test":
    c = 1

string_length(string)

s = 'hissssssssssss'
print s[1]          ## i
print len(s)        ## 2
print s + ' there'  ## hi there
    
for c in s:
    d = print 1
    
s.split()

items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(items):
    items[index] = 1
sum(items)

len(s)

def string_length(string):
    sum=0
    for c in string:
        sum += 1
    print(sum)

string_length(s)


def reverse(string):
    string=list(string)
    bstring=string[:]
    for i in range(len(string)):
        bstring[i] = string[len(string)-1-i]
    bstring = ''.join(bstring)
    print(bstring)
        
reverse('Rhiannon')