#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:55:35 2021

@author: stepianno
"""
import numpy as np
with open('flashes.txt') as f:
    content = f.readlines()
content = [[11] + [int(x) for x in line.strip()] + [11] for line in content]
octos = np.vstack((np.array([11]*12) ,np.array(content), np.array([11]*12)))
bursts = 0
def burst(y, x):
    octos[y, x] = 0
    adj = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]
    for j, i in adj:
        if 10 > octos[y+j, x+i] > 0:
            octos[y+j, x+i] += 1
i = 0
while not np.all(octos[1:10, 1:10] == 0):
    octos += 1
    while np.any(octos == 10):
        ys, xs = np.where(octos == 10)
        burst(ys[0], xs[0])
        bursts += 1
    i += 1
    if i == 100:
        print('part a:', bursts)
print('part b:', i)