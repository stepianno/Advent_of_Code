#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:59:21 2022

@author: stepianno
"""

import numpy as np
with open('trees.txt') as f:
    trees = np.array([[int(y) for y in x.strip()] for x in f.readlines()])

visible = len(trees)*2 + (len(trees[0])-2)*2
max_score = 0
for j in range(1, len(trees)-1):
    for i in range(1, len(trees[0])-1):
        h = trees[j,i]
        if np.max(trees[j,i+1:]) < h or np.max(trees[j,:i]) < h or np.max(trees[:j,i]) < h or np.max(trees[j+1:,i]) < h:
            visible += 1
        down = trees[j,i+1:]
        right = trees[j+1:,i]
        up = np.flip(trees[j,:i])
        left = np.flip(trees[:j,i])
        score = 1
        for arr in [up, down, left, right]:
            if len(np.where(arr >= h)[0]):
                score *= np.min(np.where(arr >= h)) + 1
                val = np.min(np.where(arr >= h)) + 1
            else:
                score *= len(arr)
                val = len(arr)
        max_score = max(score, max_score)
print('Part 1:', visible)
print('Part 2:', max_score)