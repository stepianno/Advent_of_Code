#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:05:20 2020

@author: stepianno
"""

with open('jolts.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
content.sort()
content = [0] + content + [max(content) + 3]

jolts = {1:0, 3:0}
j = min(content)
jolt_groups = [] #for part 2, there's only one option if the adapters are 
                 #separated by 3 jolts. I group them if they are separated by 1
                 #so my recursion function can actually work on smaller groups
                 #since the whole list is too much to ever finish.
jolt_group = [0]
for jolt in content[1:]:
    jolts[jolt - j] += 1
    if jolt - j == 1:
        jolt_group.append(jolt)
    else:
        jolt_groups.append(jolt_group)
        jolt_group = [jolt]
    j = jolt
    
print(jolts[1]*jolts[3])

def count_arrangements(content):
    if len(content) == 1:
        return 1
    count = 0
    for i in range(1,len(content)):
        if content[i] - content[0] <= 3:
            count += count_arrangements(content[i:])
        else:
            break
    return count

total = 1
for jolt_group in jolt_groups:
    total *= count_arrangements(jolt_group)
    
print(total)
    

def count_arrangements2(content):
    '''I did not come up with this method. Credit goes to 
    https://github.com/spencer-zepelin/AoC/blob/main/2020/10/pt2.py
    I learned a lot by looking at this solution'''
    paths = {}
    paths[0] = 1
    for jolt in content[1:]:
        paths[jolt] = paths.get(jolt-1, 0) + paths.get(jolt-2,0) + paths.get(jolt-3,0)
    return paths[content[-1]]