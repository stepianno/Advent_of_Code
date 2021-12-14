#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:06:33 2021

@author: stepianno
"""

from collections import Counter
with open('polymers.txt') as f:
    code, polys = f.read().split('\n\n')
code = code.strip()
polys = [poly.strip().split(' -> ') for poly in polys.strip().split('\n')]
poly_dict= {}
for poly, l in polys:
    poly_dict[poly] = l
counts = Counter(code)
pair_counts = Counter([a + b for a, b in zip(code, code[1:])])
for _ in range(40):
    new_pair_counts = Counter()
    for poly, n in pair_counts.items():
        letter = poly_dict[poly]
        counts[letter] += n
        new_pair_counts[poly[0]+letter] += n
        new_pair_counts[letter+poly[1]] += n
    pair_counts = new_pair_counts
    if _ == 9:
        print('part a:', max(counts.values()) - min(counts.values()))
print('part b:', max(counts.values()) - min(counts.values()))