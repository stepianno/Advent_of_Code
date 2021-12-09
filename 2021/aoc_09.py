#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:59:09 2021

@author: stepianno
"""

import numpy as np
from collections import defaultdict
with open('map.txt') as f:
    content = f.readlines()
lava = [[9] + [int(x) for x in line.strip()] + [9] for line in content]
lava = np.array(lava)
lava = np.vstack((np.array([9]*len(lava[0])), lava, np.array([9]*len(lava[0]))))
mins = []
adj = [(1,0), (-1,0), (0,1), (0,-1)]
for i in range(1, len(lava) - 1):
    for j in range(1, len(lava[0]) - 1):
        local = True
        for y, x in adj:
            if lava[i+y, j+x] <= lava[i, j]:
                local = False
                break
        if local:
            mins.append(lava[i, j]+1)
print('part a:', sum(mins))

inds = np.where(lava != 9)
basins = np.zeros(lava.shape)
basins[inds] = 1
basin = 0
basin_dict = defaultdict(int)
coords = {}
def basin_check(x, y):
    if (x, y) in coords or basins[y, x] == 0:
        return
    else:
        coords[(x, y)] = basin
        basin_dict[basin] += 1
    for i, j in adj:
        basin_check(x+i, y+j)

for i in range(1, len(lava) - 1):
    for j in range(1, len(lava[0]) - 1):
        if (j, i) not in coords and basins[i, j] == 1:
            basin += 1
        basin_check(j, i)
basin_sizes = list(basin_dict.values())
basin_sizes.sort(reverse=True)
print('part b:', np.prod(basin_sizes[:3]))