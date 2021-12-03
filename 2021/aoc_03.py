#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:55:20 2021

@author: stepianno
"""
from collections import Counter
with open('bin.text') as f:
    content = f.readlines()
content = [x.strip() for x in content]
gamma = ''
epsilon = ''

for i in range(len(content[0])):
    ls = [x[i] for x in content]
    count = Counter(ls)
    if count['0'] > count['1']:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print('part a:', int(gamma, 2) * int(epsilon, 2))

oxy = content[:]
c02 = content[:]
for i in range(len(content[0])):
    if len(oxy) > 1:
        ls = [x[i] for x in oxy]
        oxy_count = Counter(ls)
        if oxy_count['0'] > oxy_count['1']:
            oxy = [x for x in oxy if x[i] == '0']
        else:
            oxy = [x for x in oxy if x[i] == '1']
    if len(c02) > 1:      
        lst = [x[i] for x in c02]
        c02_count = Counter(lst)
        if c02_count['1'] < c02_count['0']:
            c02 = [x for x in c02 if x[i] == '1']
        else:
            c02 = [x for x in c02 if x[i] == '0']
print('part b:', int(oxy[0], 2) * int(c02[0], 2))