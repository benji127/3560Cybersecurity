#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Enea Paja  
# 2023/04/06

f=open("access.log", "r")

#Read
while True:
    line=f.readline()
    if not line:
        break
    #check for 404
    if "404" in line:
        print(line.strip())
        
    print(line.count())    
f.close()