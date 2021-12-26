#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:02:50 2021

@author: stepianno
"""
import re
import numpy as np
with open('blocks.txt') as f:
    content = f.readlines()
# content = '''on x=10..12,y=10..12,z=10..12
# on x=11..13,y=11..13,z=11..13
# off x=9..11,y=9..11,z=9..11
# on x=10..10,y=10..10,z=10..10'''.splitlines()
instr, blocks = zip(*[line.split() for line in content])
blocks = [[[int(n) for n in re.findall('-?\d+', a)] for a in line.split(',')] for line in blocks]
cubes = np.zeros((101,101,101))
for i in range(len(instr)):
    todo = instr[i]
    xs, ys, zs = np.array(blocks[i])+50
    if any([a>100 or a<0 for a in np.hstack((xs,ys,zs))]):
        continue
    if todo == 'on':
        cubes[zs[0]: zs[1]+1, ys[0]: ys[1]+1, xs[0]: xs[1]+1] = 1
    else:
        cubes[zs[0]: zs[1]+1, ys[0]: ys[1]+1, xs[0]: xs[1]+1] = 0
print('part a:', np.sum(cubes))

prisms = []
for i in range(len(instr)):
    todo = instr[i]
    xns, yns, zns = blocks[i]
    new_prisms = []
    for prism in prisms:
        xos, yos, zos = prism
        if ((xos[0] <= xns[0] <= xos[1] or xos[0] <= xns[1] <= xos[1]
             or xns[0] <= xos[0] <= xns[1] or xns[0] <= xos[1] <= xns[1]) and
            (yos[0] <= yns[0] <= yos[1] or yos[0] <= yns[1] <= yos[1] or
             yns[0] <= yos[0] <= yns[1] or yns[0] <= yos[1] <= yns[1]) and 
            (zos[0] <= zns[0] <= zos[1] or zos[0] <= zns[1] <= zos[1] or
             zns[0] <= zos[0] <= zns[1] or zns[0] <= zos[1] <= zns[1])):
            if xos[0] < xns[0] <= xos[1]:
                new_prisms.append(((xos[0], xns[0]-1), yos, zos))
                xos = (xns[0], xos[1])
            if xos[0] <= xns[1] < xos[1]:
                new_prisms.append(((xns[1]+1, xos[1]), yos, zos))
                xos = (xos[0], xns[1])
            if yos[0] < yns[0] <= yos[1]:
                new_prisms.append((xos, (yos[0], yns[0]-1), zos))
                yos = (yns[0], yos[1])
            if yos[0] <= yns[1] < yos[1]:
                new_prisms.append((xos, (yns[1]+1, yos[1]), zos))
                yos = (yos[0], yns[1])
            if zos[0] < zns[0] <= zos[1]:
                new_prisms.append((xos, yos, (zos[0], zns[0]-1)))
                zos = (zns[0], zos[1])
            if zos[0] <= zns[1] < zos[1]:
                new_prisms.append((xos, yos, (zns[1]+1, zos[1])))
                zos = (zos[0], zns[1])
        else:
            new_prisms.append(prism)
    if todo == 'on':
        new_prisms.append((xns, yns, zns))
    prisms = new_prisms.copy()
                
total = 0
for prism in prisms:
    xs, ys, zs = prism
    total += ((xs[1]-xs[0]+1) * (ys[1]-ys[0]+1) * (zs[1]-zs[0]+1))
print('part b:', total)
                        
                        
                        
                        