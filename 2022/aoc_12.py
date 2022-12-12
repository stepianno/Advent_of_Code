#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:04:26 2022

@author: stepianno
"""
import numpy as np
with open('elevation.txt') as f:
    data = [x.strip() for x in f.readlines()]
data = np.array([[ord(c)-97 for c in line] for line in data])
start = np.where(data == ord('S')-97)
s_j, s_i = start[0][0], start[1][0]
end = np.where(data == ord('E')-97)
e_j, e_i = end[0][0], end[1][0]
data[start] = 0
data[end] = 25
steps = np.zeros(data.shape) + float('inf')

def move(j, i, step=0, level=0):
    next_level = data[j, i]
    if next_level > level + 1:
        return
    if step >= steps[j, i]:
        return
    else:
        steps[j, i] = step
    if j > 0:
        move(j-1, i, step+1, next_level)
    if j < data.shape[0]-1:
        move(j+1, i, step+1, next_level)
    if i > 0:
        move(j, i-1, step+1, next_level)
    if i < data.shape[1]-1:
        move(j, i+1, step+1, next_level)
        
move(s_j, s_i)
print('Part 1:', steps[e_j, e_i])

zeros = np.where(data == 0)
for k in range(len(zeros[0])):
    move(zeros[0][k], zeros[1][k])
print('Part 2:', steps[e_j, e_i])