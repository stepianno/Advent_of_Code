#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 19:20:06 2023

@author: stepianno
"""

import numpy as np
with open('aoc_13_input.txt') as f:
    data = f.read().split('\n\n')

data = [[list(row) for row in pattern.strip().split('\n')] for pattern in data]
total = 0
for pattern in data:
    pattern = np.array(pattern)
    height, width = pattern.shape
    vert = False
    for n in range(width - 1):
        i = n
        j = i+1
        flag = False
        while i >= 0 and j < width:
            if np.array_equal(pattern[:,i], pattern[:,j]):
                i -= 1
                j += 1
            else:
                flag = True
                break
        if flag:
            continue
        total += n+1
        vert = True
        break
    if not vert:
        for n in range(height - 1):
            i = n
            j = i+1
            flag = False
            while i >= 0 and j < height:
                if np.array_equal(pattern[i], pattern[j]):
                    i -= 1
                    j += 1
                else:
                    flag = True
                    break
            if flag:
                continue
            total += 100*(n+1)
            break
print(total)                
total = 0
for pattern in data:
    pattern = np.array(pattern)
    height, width = pattern.shape
    vert = False
    for n in range(width - 1):
        i = n
        j = i+1
        smudge = False
        flag = False
        while i >= 0 and j < width:
            if np.array_equal(pattern[:,i], pattern[:,j]):
                i -= 1
                j += 1
            elif not smudge:
                smudge = True
                for a in range(height):
                    if pattern[a,i] != pattern[a,j]:
                        copy = np.copy(pattern[:,i])
                        copy[a] = pattern[a,j]
                        if np.array_equal(copy, pattern[:,j]):
                            i -= 1
                            j += 1
                        break
            else:
                flag = True
                break
        if flag:
            continue
        elif smudge:
            total += n+1
            vert = True
            break
    if not vert:
        for n in range(height - 1):
            i = n
            j = i+1
            smudge = False
            flag = False
            while i >= 0 and j < height:
                if np.array_equal(pattern[i], pattern[j]):
                    i -= 1
                    j += 1
                elif not smudge:
                    smudge = True
                    for a in range(width):
                        if pattern[i,a] != pattern[j, a]:
                            copy = np.copy(pattern[i,:])
                            copy[a] = pattern[j, a]
                            if np.array_equal(copy, pattern[j]):
                                i -= 1
                                j += 1
                            break
                else:
                    flag = True
                    break
            if flag:
                continue
            elif smudge:
                total += 100*(n+1)
                break
print(total)
                
                
                
                