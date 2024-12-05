#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:53:08 2024

@author: stepianno
"""

with open("aoc_04_input.txt") as f:
  data = f.read()

data = [list(row) for row in data.splitlines()]
found = 0
found2 = 0
def xmas(j, i, y, x):
    if j + 3*y >= len(data) or j + 3*y < 0 or i + 3*x >= len(data[0]) or i + 3*x < 0:
        return False
    for c in ['M', 'A', 'S']:
        j += y
        i += x
        if data[j][i] != c:
            return False
    return True

def masses(j, i):
    if j == 0 or j == len(data) -1 or i == 0 or i == len(data[0]) - 1:
        return False
    check = [(1,1), (-1,1)]
    for y, x in check:
        if not ((data[j+y][i+x] == 'M' and data[j-y][i-x] == 'S') or \
                (data[j+y][i+x] == 'S' and data[j-y][i-x] == 'M')):
            return False
    return True

vec = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
for j in range(len(data)):
    for i in range(len(data[0])):
        if data[j][i] == 'X':
            for y, x in vec:
                found += xmas(j, i, y, x)
        elif data[j][i] == 'A':
            found2 += masses(j, i)
print('Part 1:', found)
print('Part 2:', found2)