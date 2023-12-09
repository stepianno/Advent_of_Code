#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:55:28 2023

@author: stepianno
"""

with open('aoc_09_input.txt') as f:
    data = f.read()

data = [[int(x) for x in line.strip().split()] for line in data.strip().split('\n')]
total = 0
total2 = 0
for line in data:
    h = [line]
    s = line
    while any(s):
        s = [b - a for a, b in zip(s[:-1], s[1:])]
        h.append(s)
    n = sum([line[-1] for line in h])
    total += n
    p = 0
    for line in h[::-1]:
        p = line[0] - p
    total2 += p
print('Part 1:', total)
print('Part 2:', total2)