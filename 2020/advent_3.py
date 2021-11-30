#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:05:21 2020

@author: stepianno
"""

def tree_path(data, right, down, i=0, j=0, trees=0):
    if j >= len(data[i]):
        j -= len(data[i])
    if data[i][j] == '#':
        trees += 1
    if data[i] == data[-1]:
        return trees
    else:
        return tree_path(data, right, down, i+down, j+right, trees)

with open('trees.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

trees = 1
for i in range(1,9,2):
    trees *= tree_path(content, i, 1)
    
trees *= tree_path(content, 1, 2)
print(trees)