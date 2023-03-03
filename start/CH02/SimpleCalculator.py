#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created 

import math
#get inputs for the user first
#Note we are casting numbers as "float", we could also do "int"

first_num = float(input("Enter first number: "))
activity = input("Enter activity(+ - * /): ")
second_num = float(input("Enter second number: "))

if activity == "+":
    result = first_num + second_num
if activity == "-":
    result = first_num - second_num
if activity == "*":
    result = first_num * second_num
if activity == "/":
    result = first_num / second_num

print(f"The result is {result}")