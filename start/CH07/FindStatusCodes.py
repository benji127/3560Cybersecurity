#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By Enea Paja  
# 

#Import Python modules
import re

# Prompt for file to analyze
log_file = input("Which file to analyze? ")

# Open file and load into memory
with open(log_file, "r") as f:
    sample_logs = f.readlines()

# Setup regex pattern and empty dictionary
#Find a string of 3 consecutive numbers and uses white spaces so it can avoid the IP address
status_pattern = r'\s(\d{3})\s'
statusdict = {}

# Find match and store in dictionary
for line in sample_logs:
    # Search for pattern, and if found move forward. It matches the first instances of the line not all the occurrencies.And count only that.
    
    m = re.search(status_pattern, line)
    if m:
        client = m.group()
        # Put access frequency in dictionary
        if client in statusdict.keys():
            statusdict[client] += 1
        else:
            statusdict[client] = 1


# Sort by most frequently accessed
for w in sorted(statusdict, key=statusdict.get, reverse=False):
    print(w, statusdict[w])
