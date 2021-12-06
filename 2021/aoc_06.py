#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:03:50 2021

@author: stepianno
"""
from collections import Counter
with open('fish.txt') as f:
    content = f.read()
content = content.strip()
fish = [int(x) for x in content.split(',')]


def fish_count(r):
    counts = Counter(fish)
    for _ in range(r):
        new_counts = Counter()
        for k, v in counts.items():
            if k > 0:
                new_counts[k-1] += v
            else:
                new_counts[6] = v.real + v.imag
                new_counts[1] += complex(0,v.real)
        counts = new_counts.copy()
    return int(sum([v.real + v.imag for v in counts.values()]))

print('part a:', fish_count(80))
print('part b:', fish_count(256))