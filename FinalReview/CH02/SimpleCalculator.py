#!/usr/bin/env python3

import math

first_num=float(input("Num1"))
activity = input("Enter the operand")
sec_num=float(input("Num2"))

if activity == "+":
    result = first_num + sec_num
if activity == "-":
    result = first_num - sec_num
if activity == "*":
    result = first_num * sec_num
if activity == "/":
    result = first_num / sec_num3
    
print(f"The result is: {result}")