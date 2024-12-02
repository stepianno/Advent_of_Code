#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 08:42:02 2024

@author: stepianno
"""
from collections import Counter

with open("aoc_01_input.txt") as f:
  data = f.readlines()

data = [x.split() for x in data]
a = [int(x[0]) for x in data]
b = [int(x[1]) for x in data]
a.sort()
b.sort()
difs = 0
for i in range(len(a)):
    difs += abs(a[i] - b[i])
print('part 1:', difs)

counts = Counter(b)
sims = 0
for n in a:
    sims += n * counts[n]
print('part 2:', sims)