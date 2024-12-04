#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:17:48 2024

@author: stepianno
"""

import re

with open("aoc_03_input.txt") as f:
  data = f.read()

total = 0
total2 = 0
flag = True
muls = re.findall('(mul\(\d{1,3},\d{1,3}\)|do(?:n\'t)?\(\))', data)

for mul in muls:
    vals = re.findall('\d+', mul)
    n = 1
    n2 = 1
    if len(vals):
        for val in vals:
            n *= int(val)
            if flag:
                n2 *= int(val)
        total += n
        if flag:
            total2 += n2
    elif mul == 'do()':
        flag = True
    elif mul == 'don\'t()':
        flag = False        
        

print('part 1:', total)
print('part 2:', total2)