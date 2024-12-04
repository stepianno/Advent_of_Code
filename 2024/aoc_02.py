#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:00:19 2024

@author: stepianno
"""

with open("aoc_02_input.txt") as f:
  data = f.readlines()

def check(ns, l=True, k=True):
    w = True if ns[0] < ns[1] else False
    for i in range(len(ns) - 1):
        d = ns[i+1] - ns[i]
        if (abs(d) > 3 or d == 0) or (w and d < 0) or (not w and d > 0):
            if l:
                return False
            else: 
                for j in range(len(ns)):
                    line = ns[:j] + ns[j+1:]
                    if check(line):
                        return True
                return False
    return True

good = 0
good2 = 0
for line in data:
    line = [int(x) for x in line.split()]
    good += check(line)
    good2 += check(line, l=False)
    
print('part 1:', good)    
print('part 2:', good2)