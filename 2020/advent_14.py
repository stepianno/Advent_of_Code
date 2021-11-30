#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 23:15:03 2020

@author: stepianno
"""
import re

with open('masks.txt') as f:
    content = f.readlines()
content = [x.strip()for x in content]

masks = []
mems = []
mem = {}
for line in content:
    if re.search('mask', line):
        masks.append(line.split(' = ')[1])
        if mem:
            mems.append(mem)
            mem = {}
    else:
        nums = re.findall('\d+', line)
        mem[nums[0]] = nums[1]
mems.append(mem)

memo = {}
for i in range(len(masks)):
    for k,v in  mems[i].items():
        binary = bin(int(v))[2:]
        mask = list(masks[i])
        x = -1
        while -x <= len(binary):
            if mask[x] == 'X':
                mask[x] = binary[x]
            x -= 1
        mask = ''.join(mask)
        mask = mask.replace('X', '0')
        memo[k] = int(mask, 2)
print(sum(memo.values()))

def all_pos(mask):
    xs = re.findall('X', mask)
    old = ['']
    for x in xs:
        new = []
        for code in old:
            new.append(code+'0')
            new.append(code+'1')
        old = new.copy()
    out = []
    for code in old:
        bit = mask
        for bi in code:
            bit = bit.replace('X', bi, 1)
        out.append(bit)
    for i in range(len(out)):
        out[i] = int(out[i], 2)
    return out

memo = {}
for i in range(len(masks)):
    for k,v in  mems[i].items():
        binary = bin(int(k))[2:]
        mask = list(masks[i])
        x = -1
        while -x <= len(binary):
            if mask[x] == '0':
                mask[x] = binary[x]
            x -= 1
        mask = ''.join(mask)
        writes = all_pos(mask)
        for write in writes:
            memo[write] = int(v)
print(sum(memo.values()))




