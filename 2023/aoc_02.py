#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 23:04:08 2023

@author: stepianno
"""

with open('aoc_02_input') as f:
    data = f.readlines()
pos = 0
total = 0
for i, line in enumerate(data, 1):
    _, rounds = line.split(': ')
    rounds = [[[a for a in x.split(' ')] for x in r.split(', ')] for r in rounds.strip().split('; ')]
    tops = {'red': 0, 'green':0, 'blue':0}
    for game in rounds:
        for pull in game:
            n, color = pull
            n = int(n)
            if n > tops[color]:
                tops[color] = n
    if tops['red'] <= 12 and tops['green'] <= 13 and tops['blue'] <= 14:
        pos += i
    power = tops['red'] * tops['green'] * tops['blue']
    total += power
print('Part 1:', pos)
print('Part 2:', total)