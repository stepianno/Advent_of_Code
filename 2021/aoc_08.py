#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:00:13 2021

@author: stepianno
"""
import re
with open('segments.txt') as f:
    content = f.readlines()
content = [line.strip() for line in content]
output = [line.split(' | ')[1].split() for line in content]
uniques = [[x for x in line if len(x) not in [5,6]] for line in output]
print('part a:', sum([len(x) for x in uniques]))

total = 0
for line in content:
    case = line.split()[:10]
    num_dict = {}
    for sig in case:
        if len(sig) == 2:
            num_dict[1] = sig
        elif len(sig) == 3:
            num_dict[7] = sig
        elif len(sig) == 4:
            num_dict[4] = sig
        elif len(sig) == 7:
            num_dict[8] = sig
    for char in num_dict[1]:
        ls = []
        for l in case:
            if char not in l:
                ls.append(l)
        if len(ls) == 1:
            num_dict[2] = ls[0]
        elif len(ls) == 2:
            for l in ls:
                if len(l) == 5:
                    num_dict[5] = l
                else:
                    num_dict[6] = l
    bl = [x for x in num_dict[6] if x not in num_dict[5]][0]
    for v in num_dict.values():
        case.remove(v)
    last = []
    for l in case:
        if bl not in l:
            last.append(l)
    for l in last:
        if len(l) == 5:
            num_dict[3] = l
        elif len(l) == 6:
            num_dict[9] = l
        case.remove(l)
    num_dict[0] = case[0]
    output = line.split()[-4:]
    nums = []
    for n in output:
        for k,v in num_dict.items():
            check = '^[' + v + ']' +'{' + str(len(v)) + '}$'
            if re.search(check, n):
                nums.append(k)
    total += int(''.join([str(x) for x in nums]))
print('part b:', total)