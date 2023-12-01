#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:55:59 2023

@author: stepianno
"""

import re
with open('aoc_01_input.txt') as f:
    data = f.readlines()

total1 = 0
total2 = 0
nums = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        }
l = '(' + '|'.join(nums.keys()) + '|\d)'
f = '(' + '|'.join([x[::-1] for x in nums.keys()]) + '|\d)'
for i, line in enumerate(data):
    a1 = re.search('\d', line).group()
    b1 = re.search('\d', line[::-1]).group()
    n1 = a1 + b1
    total1 += int(n1)
    a2 = re.search(l, line).group()
    b2 = re.search(f, line[::-1]).group()[::-1]
    if a2 in nums:
        a2 = nums[a2]
    if b2 in nums:
        b2 = nums[b2]
    n2 = a2 + b2
    total2 += int(n2)
print('part 1:', total1)
print('part 2:', total2)