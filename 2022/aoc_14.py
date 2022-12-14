#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:01:50 2022

@author: stepianno
"""
import numpy as np
with open('cave.txt') as f:
    data = [x.strip() for x in f.readlines()]

data = [[y.split(',') for y in x.split(' -> ')] for x in data]
data = [[[int(a), int(b)] for a, b in row] for row in data]
max_x = max([max([x[0] for x in row]) for row in data])*2
max_y = max([max([x[1] for x in row]) for row in data])
cave = np.zeros((max_y+1, max_x))
for line in data:
    for left, right in zip(line, line[1:]):
        x1, y1 = left
        x2, y2 = right
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            cave[y1:y2+1,x1] = 1
        else:
            x1, x2 = min(x1, x2), max(x1, x2)
            cave[y1,x1:x2+1] = 1
sand = 0
y = 0
x = 500
while y < max_y and x >= 0 and x < max_x:
    if not cave[y+1, x]:
        y += 1
    elif not cave[y+1, x-1]:
        y += 1
        x -= 1
    elif not cave[y+1, x+1]:
        y += 1
        x += 1
    else:
        cave[y, x] = 1
        y = 0
        x = 500
        sand += 1
print('Part 1:', sand)
floor = np.zeros((2, max_x))
floor[1,:] = 1
cave = np.vstack((cave, floor))
y = 0
x = 500
while True:
    if not cave[y+1, x]:
        y += 1
    elif not cave[y+1, x-1]:
        y += 1
        x -= 1
    elif not cave[y+1, x+1]:
        y += 1
        x += 1
    else:
        cave[y, x] = 1
        sand += 1
        if y == 0:
            break
        y = 0
        x = 500
print('Part 2:', sand)
        