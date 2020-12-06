#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 22:55:40 2020

@author: stepianno
"""

with open('customs.txt') as f:
    content = f.read()
content = content.split('\n\n')
groups = [x.splitlines() for x in content]
    
from collections import Counter

count = 0
for group in groups:
    counter = Counter()
    for ind in group:
        counter += Counter(ind)
    count += len(counter)
    
print(count)

real_count = 0
for group in groups:
    counted = Counter()
    for ind in group:
        counted += Counter(ind)
    real_count += len([a for a in counted.values() if a==len(group)])
    
print(real_count)