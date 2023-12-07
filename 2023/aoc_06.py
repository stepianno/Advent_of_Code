#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:48:18 2023

@author: stepianno
"""

import math
races = [(47,400), (98,1213), (66,1011), (98,1540)]
prod = 1
for t, y in races:
    y += 1
    low = math.ceil((t - math.sqrt(t**2 - 4*y))/2)
    high = math.floor((t + math.sqrt(t**2 - 4*y))/2)
    prod *= (high-low)+1
print('Part 1:', prod)

t = int(''.join([str(x[0]) for x in races]))
y = int(''.join([str(x[1]) for x in races])) + 1
low = math.ceil((t - math.sqrt(t**2 - 4*y))/2)
high = math.floor((t + math.sqrt(t**2 - 4*y))/2)
print('Part 2:', high - low + 1)