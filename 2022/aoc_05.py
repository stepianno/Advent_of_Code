#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:21:33 2022

@author: stepianno
"""
from collections import defaultdict
import re
with open('crates.txt') as f:
    crates, moves = f.read().split('\n\n')

crates = crates.replace('[', ' ').replace(']', ' ')
crates = [list(line) for line in crates.split('\n')]
crate_dict = defaultdict(list)
for line in crates[:-1]:
    for i in range(1, len(line), 4):
        crate = int((i - 1)/4 + 1)
        if line[i] != ' ':
            crate_dict[crate] = [line[i]] + crate_dict[crate]
crate_dict2 = {}
for i in range(1, 10):
    crate_dict2[i] = crate_dict[i][:]
    
moves = [[int(y) for y in re.findall('\d+', x)] for x in moves.strip().split('\n')]
for count, start, end in moves:
    for i in range(count):
        crate_dict[end].append(crate_dict[start].pop(-1))
    crate_dict2[end] += crate_dict2[start][-count:]
    crate_dict2[start] = crate_dict2[start][:-count]
string = ''
string2 = ''
for i in range(1,10):
    string += crate_dict[i][-1]
    string2 += crate_dict2[i][-1]
print('Part 1:', string)
print('Part 2:', string2)