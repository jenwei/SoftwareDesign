# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:18:13 2014

@author: jenwei
"""

def print_plus():
    print '+',
    
def print_dash():
    print '-',
    
def print_line():
    print '|',
    
def print_space():
    print ' ',
    
def do_twice(f):
    f()
    f()

def do_three(f):
    f()
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)
    
def start_new_line():
    print

def print_plus_row():
    print_plus()
    do_four(print_dash)
    print_plus()
    do_four(print_dash)
    print_plus()
    start_new_line()
    
def print_line_row():
    print_line()
    do_four(print_space)
    print_line()
    do_four(print_space)
    print_line()
    start_new_line()
    
print_plus_row()
do_four(print_line_row)
print_plus_row()
do_four(print_line_row)
print_plus_row()