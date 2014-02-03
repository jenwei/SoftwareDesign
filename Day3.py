# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:19:27 2014

@author: jwei
"""
import math

#Chapter 2 Question 1
print 'aaaaaaaaaab'*5 + "\n" + 'daaaaaaaaaac'*5


#Chapter 2 Question 1 Alternate Solution
z = 'a'*10
print (z+'b')*5
print('d'+z+'c')*5


#Conditional Question 1
x = 199

if x>=0 and x<=100:
    print "hello"
elif x>100 and x<500:
    print "goodbye"
elif x>=500 and x<=1000:
    print "ciao"
    
#Conditional Question 2
y = '01052'
x = 5

if (x>=0 and x<=100) or  y == '01052':
    print "yes"
    
#Calling Functions
print abs(-4)
print float(35)

#Creating your own functions
def hello_world():
    print "Hello, world!"
hello_world()

def print_absolute_value(x):
    print str(abs(x))
    
print_absolute_value(-5)

#cyof Exercise 1

def hypotenuse(a,b):
    print math.sqrt(a**2 +b**2)
    
hypotenuse(3,4)

#Exercise 3-3
def right_justify(s):
    print " "*(70-len(s)) + s
    # print 'a'*70 use to check that right_justify actually shifts the string to the 70th column
    
right_justify('allen')

#Exercise 3-4
#def do_twice(f):
#    f()
#    f()

#def print_spam():
#    print 'spam'
    
#do_twice(print_spam)

#Exercise 3-4 Alternative
def print_twice(s):
    print s

def do_twice(f,arg):
    f(arg)
    f(arg)

def do_four(f,arg):
    do_twice(do_twice(f,arg))

do_four(print_twice, "potato")

#Basics of Fruitful Function
def my_absolute_value(x):
    return abs(x)
print my_absolute_value(-500)
