#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:16:38 2021

@author: stepianno
"""

with open('depth.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

#part 1
increase = 0
current = content[0]
for d in content:
    if d > current:
        increase += 1
    current = d
print('part 1:', increase)

increase = 0
current = sum(content[:3])
for i in range(len(content) - 2):
    if sum(content[i:i+3]) > current:
        increase += 1
    current = sum(content[i:i+3])
print('part 2:', increase)