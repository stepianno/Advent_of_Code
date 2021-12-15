#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 00:43:13 2021

@author: stepianno
"""

import numpy as np
with open('risk.txt') as f:
    risk = [[int(x) for x in line.strip()] for line in f.readlines()]
risk = np.array(risk)
def solve(risk):
    shape = risk.shape
    counts = np.zeros(shape)
    for j in range(shape[0]):
        for i in range(shape[1]):
            if i==0 and j==0:
                continue
            if j==0:
                counts[j,i] = risk[j,i] + counts[j,i-1]
            elif i==0:
                counts[j,i] = risk[j,i] + counts[j-1,i]
            else:
                counts[j,i] = risk[j,i] + min(counts[j-1,i], counts[j,i-1])
    def nei_check(y,x):
        adj = [(1,0),(-1,0),(0,1),(0,-1)]
        for j,i in adj:
            if counts[y,x] > risk[y,x] + counts[min(shape[0]-1, max(0,y+j)),min(shape[1]-1,max(0,x+i))]:
                counts[y,x] = risk[y,x] + counts[y+j,x+i]
    while True:
        count_back = counts.copy()
        for j in range(shape[0]):
            for i in range(shape[1]):
                nei_check(j,i)
        if np.array_equal(counts, count_back):
            break
    return counts[-1,-1]

print('part a:', solve(risk))

last = risk.copy()
for _ in range(4):
    h = last + 1
    tens = np.where(h==10)
    h[tens] = 1
    risk = np.hstack((risk, h))
    last = h.copy()
last = risk.copy()
for _ in range(4):
    v = last + 1
    tens = np.where(v==10)
    v[tens] = 1
    risk = np.vstack((risk, v))
    last = v.copy()
print('part b:', solve(risk))
            
        