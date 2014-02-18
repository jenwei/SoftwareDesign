# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:30:01 2014

@author: jenwei
"""

def compare(x,y):
    if x>y: return 1    # restructure using if/else
    if x==y: return 0
    if x<y: return -1

'''
This totally works for what you're supposed to do,
but normally, you should structure your conditionals
using if/else statements, especially if the variables 
you're comparing are the same variables each time.
'''