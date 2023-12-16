#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:51:40 2023

@author: stepianno
"""
from collections import defaultdict
data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'.split(',')
with open('aoc_15_input.txt') as f:
    data = f.read()
data = data.replace('\n', '').split(',')
total = 0
for s in data:
    x = 0
    for l in s:
        x = (ord(l)+x)*17 % 256
    total += x
print('Part 1:',total)

boxes = defaultdict(dict)
for s in data:
    i = s.index('-') if '-' in s else s.index('=')
    label = s[:i]
    box = 0
    for l in label:
        box = (ord(l)+box)*17 % 256
    if s[i] == '-':
        boxes[box].pop(label, None)
    else:
        lens = int(s[i+1:])
        boxes[box][label] = lens
total = 0
for box, labels in boxes.items():
    b = box + 1
    for i, (_, n )in enumerate(labels.items(), 1):
        total +=  b * i * n
print('Part 2:', total)