#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:24:21 2022

@author: stepianno
"""
from collections import defaultdict
with open('directories.txt') as f:
    data = [x.strip() for x in f.readlines()]

current_dir = None
level = 0
dir_dict = defaultdict(dict)
for line in data:
    if line == '$ cd ..':
        current_dir = dir_dict[current_dir]['parent']
        level -= 1
    elif '$ cd' in line:
        level += 1
        if current_dir:
            new_dir = current_dir + '/' + line.split(' ')[2]
        else:
            new_dir = line.split(' ')[2]
        dir_dict[new_dir]['parent'] = current_dir
        current_dir = new_dir
        dir_dict[current_dir]['children'] = []
        dir_dict[current_dir]['size'] = 0
        dir_dict[current_dir]['level'] = level
    elif line == '$ ls':
        continue
    elif line.split(' ')[0] == 'dir':
        dir_dict[current_dir]['children'].append(line.split(' ')[1])
    elif line.split(' ')[0].isnumeric():
            size = int(line.split(' ')[0])
            dir_dict[current_dir]['size'] += size
max_level = max([x['level'] for x in dir_dict.values()])
for i in range(max_level, 1, -1):
    depth = {k:v for k,v in dir_dict.items() if v['level'] == i}
    for k,v in depth.items():
        dir_dict[v['parent']]['size'] += v['size']
smalls = 0
needed = 30000000 - (70000000 - dir_dict['/']['size'])
delete = float('inf')
for v in dir_dict.values():
    if v['size'] <= 100000:
        smalls += v['size']
    if v['size'] >= needed:
        delete = min(delete, v['size'])
print('Part 1:',smalls)
print('Part 2:', delete)