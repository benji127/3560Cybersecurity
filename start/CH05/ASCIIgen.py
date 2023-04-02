#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By Enea Paja  
# 2023/04/01


for i in range(31, 127):
    print("{0}\t'{1}'".format(i,chr(i)))