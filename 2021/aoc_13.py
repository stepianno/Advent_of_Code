#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 23:00:00 2021

@author: stepianno
"""
import numpy as np
with open('dots.txt') as f:
    dots, folds = f.read().split('\n\n')
dots = [[int(x) for x in line.split(',')] for line in dots.splitlines()]
folds = [line.replace('fold along ', '').split('=') for line in folds.splitlines()]
dots = np.array(dots)
size_x = np.max(dots[:,0])+1
size_y = np.max(dots[:,1])+1
paper = np.zeros((size_y, size_x))
for x, y in dots:
    paper[y, x] = 1
first = True
for fold in folds:
    d, r = fold
    r = int(r)
    if d == 'x':
        side_1 = paper[:, :r]
        side_2 = paper[:, r+1:]
        side_1 = np.flip(side_1, axis=1)
        inds = np.where((side_1 == 1) | (side_2 == 1))
        paper = np.zeros(side_1.shape)
        paper[inds] = 1
    elif d == 'y':
        side_1 = paper[:r, :]
        side_2 = paper[r+1:, :]
        side_2 = np.flip(side_2, axis=0)
        inds = np.where((side_1 == 1) | (side_2 == 1))
        paper = np.zeros(side_1.shape)
        paper[inds] = 1
    if first:   
        first = False
        print('part a:', np.sum(paper))
print('part b:\n', paper)