#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 22:57:49 2021

@author: stepianno
"""
from statistics import median, mean
from math import floor
with open('crabs.txt') as f:
    content = f.read()
content = content.strip()
crabs = [int(x) for x in content.split(',')]

pos = round(median(crabs))
fuels = sum([abs(pos - crab) for crab in crabs])
print('part a:', fuels)

pos = floor(mean(crabs))
fuels = 0
for crab in crabs:
    dif = abs(pos - crab)
    fuel = int(dif * (dif+1) / 2)
    fuels += fuel
print('part b:', fuels)