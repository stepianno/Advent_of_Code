#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:03:21 2023

@author: stepianno
"""

with open('aoc_04_input.txt') as f:
    data = f.read()
data = [x.strip() for x in data.strip().split('\n')]
points = 0
scratches = {}
for i in range(1, len(data)+1):
    scratches[i] = 1
for i, row in enumerate(data, 1):
    _, nums = row.split(': ')
    wins, own = nums.split(' | ')
    wins = [int(x.strip()) for x in wins.strip().split()]
    own = [int(x.strip()) for x in own.strip().split()]
    card = 0
    matches = 0
    for win in wins:
        if win in own:
            card = card*2 if card else 1
            matches += 1
    points += card
    for j in range(1, matches+1):
        scratches[i+j] += scratches[i]
print('Part 1:', points)
print('Part 2:', sum(scratches.values()))