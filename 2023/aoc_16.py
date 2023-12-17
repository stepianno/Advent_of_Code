#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:15:27 2023

@author: stepianno
"""

import numpy as np
from collections import defaultdict
with open("aoc_16_input.txt") as f:
  data = f.read()
data = fr'{data}'
grid = np.array([list(row.strip()) for row in data.strip().split('\n')])
move_dict = {
        'r': {
                '.': [(0,1)],
                '-': [(0,1)],
                '/': [(-1,0)],
                '\\': [(1,0)],
                '|': [(-1,0), (1,0)]
            },
        'l': {
                '.': [(0,-1)],
                '-': [(0,-1)],
                '/': [(1,0)],
                '\\': [(-1,0)],
                '|': [(-1,0), (1,0)]
            },
        'u': {
                '.': [(-1,0)],
                '-': [(0,1), (0,-1)],
                '/': [(0,1)],
                '\\': [(0,-1)],
                '|': [(-1,0)]
            },
        'd': {
                '.': [(1,0)],
                '-': [(0,1), (0,-1)],
                '/': [(0,-1)],
                '\\': [(0,1)],
                '|': [(1,0)]
            }
    }
dir_dict = {
        1: 'd',
        -1: 'u',
        1j: 'r',
        -1j: 'l'
    }
most = 0
for direction in ['r', 'u', 'l', 'd']:
    for s in range(grid.shape[0]):
        energized = np.zeros(grid.shape)
        if direction == 'r':
            start = (s, 0, 'r')
        elif direction == 'u':
            start = (grid.shape[0] - 1, s, 'u')
        elif direction == 'l':
            start = (s, grid.shape[0] - 1, 'l')
        elif direction == 'd':
            start = (0, s, 'd')
        cache = defaultdict(list)
        deck = [start]
        while len(deck):
            y, x, d = deck.pop(0)
            key = y + x*1j
            if d in cache[key]:
                continue
            cache[key].append(d)
            c = grid[y,x]
            energized[y,x] = 1
            moves = move_dict[d][c]
            for j, i in moves:
                m = j + i*1j
                j += y
                i += x
                if j >= 0 and j < grid.shape[0] and i >= 0 and i < grid.shape[1]:
                    deck.append((j, i, dir_dict[m]))
        if direction == 'r' and s == 0:
            print('Part 1:', np.sum(energized))
        if np.sum(energized) > most:
            most = np.sum(energized)
print('Part 2:', most)