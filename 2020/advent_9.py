#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 23:10:21 2020

@author: stepianno
"""

with open('preamble.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

def add_prod(nums, target):
    nums.sort()
    i = 0
    j = -1
    while nums[i] + nums[j] != target:
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return (nums[i],nums[j])

i = 0
j = 25
for _ in range(25, len(content)):
    nums = content[i:j]
    try:
        add_prod(nums, content[j])
    except:
        target = content[j]
        print(target)
    i += 1
    j += 1
        
adds = []
for n in content:
    adds.append(n)
    if sum(adds) == target:
        print(min(adds) + max(adds))
        break
    else:
        while sum(adds) > target:
            adds.pop(0)
            if sum(adds) == target:
                print(min(adds) + max(adds))
                break