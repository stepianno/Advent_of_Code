#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 22:57:49 2021

@author: stepianno
"""
from statistics import median, mean
from math import floor, ceil
with open('crabs.txt') as f:
    content = f.read()
content = content.strip()
crabs = [int(x) for x in content.split(',')]
pos = round(median(crabs))
fuels = sum([abs(pos - crab) for crab in crabs])
print('part a:', fuels)

pos_floor = floor(mean(crabs))
pos_ceil = ceil(mean(crabs))
fuel_options = []
for pos in [pos_floor, pos_ceil]:
    fuels = 0
    for crab in crabs:
        dif = abs(pos - crab)
        fuel = int(dif * (dif+1) / 2)
        fuels += fuel
    fuel_options.append(fuels)
print('part b:', min(fuel_options))