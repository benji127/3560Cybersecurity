#!/usr/bin/env python3

#example working with conditionals
# By ed Goad
# date 04/12/2023

#suggestion
# add in <, ==, > one at a time
# make each of them if statements initially
# change x and y values to test the various paths
# eventually simplify with if, elif, else

def condTest():
    x,y = 100, 10
    #First condition test, x is less tha y
    if x<y:
        print("x is less then y")
    elif x==y:
        print("x is ssame as y")
    else:
        print("x is bigger than y")    

condTest()