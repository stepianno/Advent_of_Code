#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:51:14 2023

@author: stepianno
"""

with open("aoc_21_input.txt") as f:
  data = f.read()

grid = {}
new_grid = {}
for y, row in enumerate(data.strip().splitlines()):
    for x, char in enumerate(row):
        grid[y+x*1j] = char
move = [1, -1, 1j, -1j]
spots = [k for k,v in grid.items() if v == 'S']
h, w = len(data.strip().splitlines()), len(data.strip().splitlines()[0].strip())
def pos(r):
    spots = [k for k,v in grid.items() if v == 'S']
    new_grid = {}
    for _ in range(r):
        if _ > 0:
            spots = new_grid.keys()
        new_grid = {}
        for spot in spots:
            for n in move:
                n += spot
                check = n.real % h + (n.imag % w)*1j
                if grid[check] != '#':
                    new_grid[n] = 'S'
    return len(new_grid)
print('Part 1:', pos(64))

# p = an^2 + bn + c
n0, n1, n2 = [pos(x*w + w//2) for x in range(3)]
c = n0
# n1 = a + b + c
# b = n1 - n0 - a
# n2 = 4a + 2b + c
# 4a = n2 - n0 - 2b
# 4a = n2 - n0 - 2n1 + 2n0 + 2a
# 2a = n2 + n0 - 2n1
# a = (n2 + n0 - 2n1) / 2
a = (n2 + n0 - 2*n1) // 2
b = n1 - n0 - a
steps = 26501365
n = (steps - w//2) // w
print('Part 2:', a*n**2 + b*n + c)