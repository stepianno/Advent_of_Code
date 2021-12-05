#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:03:15 2021

@author: stepianno
"""

import numpy as np
with open('vectors.txt') as f:
    content = f.readlines()
vectors = [[[int(x) for x in bit.split(',')] for bit in line.strip().split(' -> ')] for line in content]
vectors = np.array(vectors)
mat = np.zeros((np.max(vectors)+1, np.max(vectors)+1))
for v0, v1 in vectors:
    if v0[0] == v1[0]:
        s, e = v0[1], v1[1]
        if s > e:
            s, e = e, s
        for i in range(s, e+1):
            mat[i, v0[0]] += 1
    if v0[1] == v1[1]:
        s, e = v0[0], v1[0]
        if s > e:
            s, e = e, s
        for i in range(s, e+1):
            mat[v0[1], i] += 1
print('part a:', len(np.where(mat >= 2)[0]))

mat = np.zeros((np.max(vectors)+1, np.max(vectors)+1))
for v0, v1 in vectors:
    if v0[0] == v1[0]:
        s, e = v0[1], v1[1]
        if s > e:
            s, e = e, s
        for i in range(s, e+1):
            mat[i, v0[0]] += 1
    elif v0[1] == v1[1]:
        s, e = v0[0], v1[0]
        if s > e:
            s, e = e, s
        for i in range(s, e+1):
            mat[v0[1], i] += 1
    else:
        x = y = 1
        if v0[0] > v1[0]:
            x = -1
        if v0[1] > v1[1]:
            y = -1
        for i in range(abs(v0[0] - v1[0])+1):
            mat[v0[1]+i*y, v0[0]+i*x] += 1
print('part b:', len(np.where(mat >= 2)[0]))