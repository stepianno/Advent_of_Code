#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:52:21 2020

@author: stepianno
"""

with open('tickets.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

def ticket_id(ticket):
    low = 0
    high = 127
    for char in ticket[:7]:
        if char == 'F':
            high = (high - low)//2 + low
        elif char == 'B':
            low = (high - low)//2 + low + 1
    left = 0
    right = 7
    for char in ticket[7:]:
        if char == 'L':
            right = (right - left)//2 + left
        elif char == 'R':
            left = (right - left)//2 + left + 1
    return low*8+left

ids = []
for line in content:
    ids.append(ticket_id(line))
print(max(ids))

ids.sort()
for i, n in enumerate(ids[:-1]):
    if ids[i+1] > n+1:
        print(n,ids[i+1])