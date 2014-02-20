# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""
"""
@edited-by: jwei
help from: josh s
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import*

def build_random_function(min_depth, max_depth):
    # your doc string goes here
    """ 
    Takes in two inputs, min_depth and max_depth
    min_depth: specifies the minimum amount of nesting for the function
    max_depth: specifies the maximum amount of nesting of the function
    Chooses a random depth between min and max
    Runs through recursive_build_random_function using found depth
    returns: a random function
    """
    # your code goes here
    l = ["prod","cos_pi","sin_pi","x","y"]
    if min_depth>0:
        i = randint(0,2)
        if l[i]=="prod":
            return [l[i],build_random_function(min_depth-1, max_depth-1),build_random_function(min_depth-1, max_depth-1)]
        return [l[i],build_random_function(min_depth-1, max_depth-1)]
    elif max_depth == 1:
        return[l[randint(3,4)]]
    else:
        i = randint(0,4)
        if l[i]=="prod":
            return [l[i],build_random_function(min_depth-1, max_depth-1),build_random_function(min_depth-1, max_depth-1)]
        if i>=3 and i<5:
            return[l[randint(3,4)]]
        else:
            return [l[i],build_random_function(min_depth-1, max_depth-1)]
            
def evaluate_random_function(f, x, y):
    # your doc string goes here
    """
    Takes in three inputs
    randomfunction: function from brf
    x: value of x for function
    y: value of y to evaluate the function at
    Output: Value of function after plugging in x and y (float)
    """
    # your code goes here
    if f[0] == "prod":
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    if f[0] == "cos_pi":
        return cos(pi*evaluate_random_function(f[1],x,y))
    if f[0] == "sin_pi":
        return sin(pi*evaluate_random_function(f[1],x,y))
    if f[0] == "x":
        return x
    if f[0] == "y":
        return y
        
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
        Takes five inputs and finds the location of val relative to the input interval
        Output: val in output interval relative to input interval
    """
    # your code goes here
    ratio = (input_interval_end-input_interval_start)/(output_interval_end-output_interval_start)
    trans = (output_interval_start-input_interval_start)/ratio
    new_val = val/ratio + trans
    return new_val
    
#Test for build_random_function, evalutate_random_function, and remap_interval 
f=build_random_function(3, 5)
print f
print evaluate_random_function(f, 0, 1)
print remap_interval(75,50,100,0,1.0)

#Part3 - COLOR IMPLEMENTATION

#Random Functions for the Red, Green, and Blue Channels
r=build_random_function(1,10)
b=build_random_function(1,10)
g=build_random_function(1,10)
print g
im=Image.new("RGB",(350,350))
p=im.load();
for i in range(0,350):
    x = remap_interval(i,0,350.,-1,1)
    for j in range(0,350):
        y = remap_interval(j,0,350.,-1,1)
        
        
        new_r = remap_interval(evaluate_random_function(r,x,y),-1.0,1.0,0,255)
        new_g = remap_interval(evaluate_random_function(g,x,y),-1.0,1.0,0,255)
        new_b = remap_interval(evaluate_random_function(b,x,y),-1,1.0,0,255)
                
        p[i,j]=(int(new_r),int(new_g),int(new_b))

im.save('im',"JPEG")