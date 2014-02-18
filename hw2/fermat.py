# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:25:32 2014

@author: jenwei
"""
def check_fermat(a,b,c,n):
    if n>2:                         # you can combine your conditionals
        if(a**n+b**n == c**n):
            print "Holy smokes, Fermat was wrong!"
        else: print "No, that doesn't work."

'''
Excellent logic; one thing I'd recommend 
is to combine your conditionals to make it a single conditional
'''