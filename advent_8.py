#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:57:51 2020

@author: stepianno
"""

with open('codes.txt') as f:
    content = f.readlines()
codes = [x.strip() for x in content]

def acc_count(codes):
    code_dict = {}
    acc = 0
    i = 0
    while True:
        if i in code_dict:
            return acc, False
        if i >= len(codes):
            return acc, True
        code, n = codes[i].split()
        code_dict[i] = acc
        n = int(n)
        if code == 'nop':
            i += 1
        elif code == 'acc':
            acc += n
            i += 1
        elif code == 'jmp':
            i += n
print(acc_count(codes))


code_dict = {}
candidates = []
acc = 0
i = 0
while True:
    if i >= len(codes):
        print(acc)
        break
    if i in code_dict:
        break
    code, n = codes[i].split()
    code_dict[i] = acc
    n = int(n)
    j = i
    if code == 'nop':
        i += 1
    elif code == 'acc':
        acc += n
        i += 1
    elif code == 'jmp':
        candidates.append(i)
        i += n

import re
for candidate in candidates:
    codex = codes.copy()
    codex[candidate] = re.sub('jmp', 'nop', codex[candidate])
    x = acc_count(codex)
    if x[1]:
        print(x)
    

