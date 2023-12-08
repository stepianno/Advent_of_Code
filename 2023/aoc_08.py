#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:58:35 2023

@author: stepianno
"""

from collections import defaultdict
import math
with open('aoc_08_input.txt') as f:
    data = f.read()
inst, maps = data.split('\n\n')
maps = [x.strip().replace('(', '').replace(')', '').replace(', ', ' = ').split(' = ') for x in maps.strip().splitlines()]
map_dict = defaultdict(dict)
for key, left, right in maps:
    map_dict[key]['L'] = left
    map_dict[key]['R'] = right
i = 0
c = 0
key = 'AAA'
while True:
    d = inst[i]
    key = map_dict[key][d]
    i += 1
    i %= len(inst)
    c += 1
    if key == 'ZZZ':
        print('Part 1:', c)
        break
locs = [x[0] for x in filter(lambda x: x[0][2] == 'A', maps)]
zs = {}
for i in range(len(locs)):
    zs[i] = []
i = 0
c = 0
while any([len(z) < 1 for z in zs.values()]):
    next_locs = []
    d = inst[i]
    for j, loc in enumerate(locs):
        key = map_dict[loc][d]
        next_locs.append(key)
        if key[2] == 'Z':
            zs[j].append(c+1)
    i += 1
    i %= len(inst)
    c += 1
    locs = next_locs
starts = [z[0] for z in zs.values()]
print('Part 2:', math.lcm(*starts))
