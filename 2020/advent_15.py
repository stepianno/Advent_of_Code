#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:04:11 2020

@author: stepianno
"""

content = [0,13,1,16,6,17]

pos = {}

i = 0
while i < 30000000-1:
    if i < len(content)-1:
        pos[content[i]] = i
        i += 1
        continue
    elif content[i] not in pos:
        x=0
    elif content[i] in pos:
        x = i - pos[content[i]]
    content.append(x)
    pos[content[i]] = i
    i+=1
print('part a:', content[2019])
print('part b:',content[-1])