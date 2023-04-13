#!/usr/bin/usr/env python3
# example working with loops
# by Enea Paja  

def forLoop():
    for x in range(6):
        print(x)
    
def whileLoop():
    count=0
    while(count <6 ):
        print("The counter is:",count)
        count+=count

def basicLoopElse():
    for x in range(6):
        print(x)
    else:
        print("Finished")

def looArray():
    fruits=["apple", "fig","cherry"]
    for x in fruits:
        print(x)

def loopArray2():
    for x in "banana":
        print(x)
        
def loopBreak():
    fruits=["1", "2", "3"]
    for x in fruits:
        print(x)
        if x == "1":
            break
        print(x)
def loopPass():
    for letter in 'Python':
        if letter == 'h':
            pass
            print("This is a pass block")
        print("Current letter: ",letter )
    print("Good Bye") 
    
# loopPass()

def nestedLoop():
    adj = ["red", "blue", "yellow"]
    fruits = ["apple", "banana", "cherry"]
    for x in adj:
        for y in fruits:
            print(x,y)
            
# nestedLoop()