#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 23:08:30 2020

@author: stepianno
"""
import numpy as np
from itertools import product

with open('grid.txt') as f:
    content = f.readlines()
content = [['.','.','.','.','.','.']+list(x.strip())+['.','.','.','.','.','.'] for x in content]

grid = np.array(content)
filler = np.repeat('.', 6*grid.shape[1]).reshape(6, grid.shape[1])
grid = np.vstack((filler, grid, filler))
layer = np.repeat('.', grid.shape[0]**2).reshape(grid.shape[0], grid.shape[0])
grid3d = np.array([layer,layer,layer,layer,layer,grid,layer,layer,layer,layer,layer])


def neighbor_check(grid,x,y,z):
    neighbors = [n for n in list(product([-1,0,1],[-1,0,1],[-1,0,1])) if n != (0,0,0)]
    count = 0
    for i,j,k in neighbors:
        try:
            if grid[x+i,y+j,z+k] == '#':
                count += 1
        except:
            continue
        if count > 3:
            return '.'
    if count == 3:
        return '#'
    elif count == 2 and grid[x,y,z] == '#':
        return '#'
    else:
        return '.'

for _ in range(6):
    grid_copy = grid3d.copy()
    for z in range(grid3d.shape[0]):
        for y in range(grid3d.shape[1]):
            for x in range(grid3d.shape[2]):
                grid3d[z,y,x] = neighbor_check(grid_copy,z,y,x)
print('part a:',np.count_nonzero(grid3d == '#'))

def neighbor_check4d(grid,x,y,z,w):
    neighbors = [n for n in list(product([-1,0,1],[-1,0,1],[-1,0,1],[-1,0,1])) if n != (0,0,0,0)]
    count = 0
    for i,j,k,l in neighbors:
        try:
            if grid[x+i,y+j,z+k,w+l] == '#':
                count += 1
        except:
            continue
        if count > 3:
            return '.'
    if count == 3:
        return '#'
    elif count == 2 and grid[x,y,z,w] == '#':
        return '#'
    else:
        return '.'

grid4d = np.array([layer,layer,layer,layer,layer,layer,layer,layer,layer,grid,
                   layer,layer,layer,layer,layer,layer,layer,layer,layer,layer])
layer4 = np.repeat('.', grid4d.shape[0]**3).reshape(grid4d.shape[0],grid4d.shape[0],grid4d.shape[0])
grid4dim = np.array([layer4,layer4,layer4,layer4,layer4,layer4,layer4,grid4d,
                     layer4,layer4,layer4,layer4,layer4,layer4,layer4])


for _ in range(6):
    grid4_copy = grid4dim.copy()
    for w in range(grid4dim.shape[0]):
        for z in range(grid4dim.shape[1]):
            for y in range(grid4dim.shape[2]):
                for x in range(grid4dim.shape[3]):
                    grid4dim[w,z,y,x] = neighbor_check4d(grid4_copy,w,z,y,x)
print('part b:',np.count_nonzero(grid4dim == '#'))


