#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 06:34:57 2023

@author: stepianno
"""

import numpy as np
with open('aoc_10_input.txt') as f:
    data = f.read()
data = [list(l.strip()) for l in data.strip().splitlines()]
data = np.array(data)
start = np.where(data=='S')
y = start[0][0]
x = start[1][0]
start = (y,x)
pipes = {
    '|': [(-1,0), (1,0)],
    '-': [(0,-1), (0, 1)],
    'L': [(-1,0), (0, 1)],
    'J': [(-1,0), (0, -1)],
    '7': [(0,-1), (1,0)],
    'F': [(0,1), (1,0)],
    '.': [],
    'S': []
    }
locs = []
for j, i in[(-1,0),(1,0),(0,-1),(0,1)]:
    v = y+j
    h = x+i
    check = data[v,h]
    for a,b in pipes[check]:
        if a == -j and b == -i:
            locs.append((v,h))
track = [[start, locs[0]], [start, locs[1]]]
c = 1
while True:
    for i, loc in enumerate(locs):
        y, x = loc
        check = data[y,x]        
        for j, k in pipes[check]:
            v = y+j
            h = x+k
            if (v,h) == track[i][-2]:
                continue
            else:
                locs[i] = (v,h)
                track[i].append((v,h))
                break
    c += 1
    if locs[0] == locs[1]:
        print('Part 1:', c)
        break
loop = track[0] + track[1][::-1][1:-1]
'''
up: A
down: V
right: >,
left: <,
up-right: R,
down-right: M,
up-left: Y,
down-left, K
'''
for i in range(len(loop)):
    if i == len(loop) - 1:
        i = -1
    dyf = loop[i+1][0] - loop[i][0]
    dxf = loop[i+1][1] - loop[i][1]
    dyp = loop[i][0] - loop[i-1][0]
    dxp = loop[i][1] - loop[i-1][1]
    f = ''
    p = ''
    if dyf == 1:
        f = 'V'
    elif dyf == -1:
        f = 'A'
    elif dxf == 1:
        f = '>'
    elif dxf == -1:
        f = '<'
    if dyp == 1:
        p = 'V'
    elif dyp == -1:
        p = 'A'
    elif dxp == 1:
        p = '>'
    elif dxp == -1:
        p = '<'
    if f == p:
        data[loop[i]] = f
    elif p+f in ['>A', 'A>']:
        data[loop[i]] = 'R'
    elif p+f in ['>V', 'V>']:
        data[loop[i]] = 'M'
    elif p+f in ['<A', 'A<']:
        data[loop[i]] = 'Y'
    elif p+f in ['<V', 'V<']:
        data[loop[i]] = 'K'
if data[min(loop)] in '<KV':
    ups = '<KY'
    downs = '>RM'
    lefts = 'VMK'
    rights = 'ARY'
else:
    downs = '<KY'
    ups = '>RM'
    rights = 'VMK'
    lefts = 'ARY'
def enclosed(y,x):
    up = data[:y, x]
    down = data[y+1:, x]
    left = data[y, :x]
    right = data[y, x+1:]
    def check_dir(arr, good, bad):
        current = ''
        g = 0
        for c in arr:
            if c in good and current != 'good':
                current = 'good'
                g += 1
            if c in bad and current != 'bad':
                current = 'bad'
                g -= 1
        if g<= 0:
            return False
        return True
    if check_dir(up, ups, downs) and check_dir(down, downs, ups) and check_dir(left, lefts, rights) and check_dir(right, rights, lefts):
        return True
    return False
count = 0
for j in range(len(data)):
    for i in range(len(data[0])):
        if data[j,i] in 'AV<>RKMY':
            continue
        count += enclosed(j,i)
print('Part 2:', count)
    
    
    