#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:16:41 2022

@author: stepianno
"""

with open('cycles.txt') as f:
    data = [x.strip() for x in f.readlines()]

cycle = 0
val = 1
part1 = 0
screen = ''

def pixel(cycle, val):
    cycle = cycle % 40
    if abs(cycle - val) <= 1:
        return '#'
    else:
        return '.'

for row in data:
    screen += pixel(cycle, val)
    cycle += 1
    if not cycle % 40:
        screen += '\n'
    if cycle % 40 == 20:
        part1 += val * cycle
    if row != 'noop':
        _, n = row.split(' ')
        n = int(n)
        screen += pixel(cycle, val)
        cycle += 1
        if not cycle % 40:
            screen += '\n'
        if cycle % 40 == 20:
            part1 += val * cycle
        val += n
print('Part 1:', part1)
print(screen)