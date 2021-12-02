#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:57:16 2021

@author: stepianno
"""

with open('direct.txt') as f:
    content = f.readlines()
content = [x.split() for x in content]

hor, depth = 0, 0
for d, x in content:
    if d == 'forward':
        hor += int(x)
    elif d == 'down':
        depth += int(x)
    else:
        depth -= int(x)
print('part a:', hor*depth)

hor, depth, aim = 0, 0, 0
for d, x in content:
    if d == 'forward':
        hor += int(x)
        depth += int(x)*aim
    elif d == 'down':
        aim += int(x)
    else:
        aim -= int(x)
print('part b:', hor*depth)