#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 23:05:51 2020

@author: stepianno
"""
import re
from collections import defaultdict

with open('train.txt') as f:
    content = f.read()

valids, mine, tickets = content.split('\n\n')
valids = re.findall('\d+-\d+', valids)
valids = [[int(n) for n in x.split('-')] for x in valids]
numbers = []
for start, end in valids:
    numbers += list(range(start,end+1))
numbers = set(numbers)

tickets = [[int(n) for n in re.findall('\d+', ticket)] for ticket in tickets.splitlines()[1:]]
error = 0
for ticket in tickets:
    e = error
    for n in ticket:
        if n not in numbers:
            error += n
    if e != error:
        ticket.append(-1)
print('part a:',error)

classes = defaultdict(list)
for ticket in tickets:
    if ticket[-1] == -1:
        continue
    for i,n in enumerate(ticket):
        classes[i].append(n)

indexing = defaultdict(list)
for i in range(0,len(valids),2):
    for k, v in classes.items():
        x = 1
        for n in v:
            if n < valids[i][0] or n > valids[i+1][1]:
                x = 0
                break
            elif n > valids[i][1] and n < valids[i+1][0]:
                x = 0
                break
        if x:
            indexing[i/2].append(k)

pos = {}
while len(pos) < 20:
    taken = []
    for k,v in indexing.items():
        if len(v) == 1:
            taken.append(v[0])
            pos[k] = v[0]
    for n in taken:
        for k,v in indexing.items():
            if n in v:
                indexing[k].remove(n)

mine = [int(n) for n in mine.splitlines()[1].split(',')]
final = 1
for k,v in pos.items():
    if k <= 5:
        final *= mine[v]
print('part b:',final)
                




