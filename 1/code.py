import os
import sys

file = open('input.txt', 'r')
Lines = file.readlines()
 
total = 0 
s = []
for line in Lines:
    for i in line.strip():
        if not i.isalpha():
            s.append(i)
    total+=int(s[0]+s[len(s)-1])
    s=[]
print(total)

# 54239