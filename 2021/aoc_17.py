#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 06:25:02 2021

@author: stepianno
"""
from itertools import product

v = 158
h = 0
while v > 0:
    h += v
    v -= 1
print('part a:', h)

min_x = 70
pos = []
while min_x > 0:
    min_x -= 1
    x = min_x
    l = 0
    while x > 0 and l < 125:
        l += x
        x -= 1
        if x == 0 and 70 <= l <= 125:
            pos.append(min_x)

min_x = min(pos)
max_x = 125
min_y = -159
max_y = 158
combos = product(range(min_x, max_x+1), range(min_y, max_y+1))
total = 0
for x,y in combos:
    h = l = 0
    x_s, y_s = x, y
    while h >= -159 and l <= 125:
        h += y
        l += x
        y -= 1
        if x > 0:
            x -= 1
        if -121 >= h >= -159 and 70 <= l <= 125:
            total += 1
            break
print('part b:', total)