#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:27:53 2022

@author: stepianno
"""

with open('elf_pairs.txt') as f:
    pairs = [x.strip() for x in f.readlines()]
pairs = [[[int(x) for x in elf.split('-')] for elf in elves.split(',')] for elves in pairs]
count = 0
lap = 0
for elf1, elf2 in pairs:
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        count += 1
        lap += 1
    elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
        count += 1
        lap += 1
    elif elf1[0] <= elf2[0] and elf2[0] <= elf1[1]:
        lap += 1
    elif elf2[0] <= elf1[0] and elf1[0] <= elf2[1]:
        lap += 1
print('Part 1:', count)
print('Part 2:', lap)