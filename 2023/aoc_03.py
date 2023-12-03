#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:09:17 2023

@author: stepianno
"""

import re
import numpy as np
from collections import defaultdict
with open('aoc_03_input.txt') as f:
    data = f.read()
data = [x.strip() for x in data.strip().split('\n')]

data = [list(re.sub('[^\d\.\*]', '+', line)) for line in data]
data = np.array(data)
stars = np.where(np.isin(data, ['*','+']))
lim_x, lim_y = len(data), len(data[0])
been = defaultdict(list)
around = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
total = 0
total2 = 0
for i, j in zip(stars[0], stars[1]):
    gears = []
    for a, b in around:
        a += i
        b += j
        if a < 0 or b < 0 or a >= lim_x or b >= lim_y or b in been[a]:
            continue
        been[a].append(b)
        if data[a,b].isdigit():
            num = data[a,b]
            c = b
            while c > 0:
                c -= 1
                been[a].append(c)
                if data[a,c].isdigit():
                    num = data[a,c] + num
                else:
                    break
            while b < lim_y-1:
                b += 1
                been[a].append(b)
                if data[a,b].isdigit():
                    num += data[a,b]
                else:
                    break
            total += int(num)
            if data[i,j] == '*':
                gears.append(num)
    if len(gears) > 1:
        total2 += eval('*'.join(gears))
print('part 1:',total)
print('part 2:',total2)