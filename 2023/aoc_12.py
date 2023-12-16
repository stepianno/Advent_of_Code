#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:56:23 2023

@author: stepianno
"""
import time
import re
with open('aoc_12_input.txt') as f:
    data = f.read()

data = [x.strip().split() for x in data.strip().splitlines()]
for i in range(len(data)):
    pat, cont = data[i]
    cont = [int(x) for x in cont.split(',')]
    data[i] = (pat, cont)

# doesn't do part 2
def counts(pat, cont):
    if not cont and '#' not in pat:
        return 1
    elif not cont:
        return 0
    count = 0
    f = cont[0]
    cont = cont[1:]
    req = sum([x+1 for x in cont]) - 1 if cont else 0
    lim = len(pat) - req
    i = 0
    while i < lim:
        sub = pat[i:lim]
        if re.search('^[\?\#]{%d}[\.\?]' % f, sub):
            count += counts(pat[i+f+1:], cont)
        elif not cont and re.search('^[\?\#]{%d}$' % f, sub):
            count += 1
        if pat[i] == '#':
            break
        i += 1
    return count

#This one works!!!
def dynamic_counts(pat, cont):
    counts = [0]*len(pat)
    tags = [i for i, l in enumerate(pat) if l=='#']
    req = sum([x+1 for x in cont[1:]]) - 1
    lim = len(pat) - req
    first = cont[0]
    for i in range(lim-1):
        if re.search('^[\?\#]{%d}[\.\?]' % first, pat[i:lim]) and '#' not in pat[:i]:
            counts[i] = 1
    for j, c in enumerate(cont[1:-1], 1):
        start = sum([x+1 for x in cont[:j]])
        req = sum([x+1 for x in cont[j+1:]]) - 1
        lim = len(pat) - req
        level = [0]*len(pat)
        for i in range(start, lim):
            tag = max([t for t in tags if t < i]) if len([t for t in tags if t < i]) else 0
            tag = max(0,tag-cont[j-1]+1)
            if re.search('^[\?\#]{%d}[\.\?]' % c, pat[i:lim]):
                level[i] = sum(counts[tag:i - cont[j-1]])
        counts = level.copy()
    start = sum([x+1 for x in cont[:-1]])
    last = cont[-1]
    level = [0]*len(pat)
    for i in range(start, len(pat)-last+1):
        tag = max([t for t in tags if t < i]) if len([t for t in tags if t < i]) else 0
        tag = max(0,tag-cont[-2]+1)
        if re.search('^[\?\#]{%d}' % last, pat[i:]) and '#' not in pat[i+last:]:
            level[i] = sum(counts[tag:i - cont[-2]])
        if pat[i] == '#' and not any(counts[i - cont[-2]:]):
            break
    return sum(level)

start_time = time.time()
count = 0
count2 = 0
for i, (pat, cont) in enumerate(data):
    count += dynamic_counts(pat,cont)
    '''if dynamic_counts(pat,cont) != counts(pat,cont):
        print(pat, cont)'''
    pat2 = '?'.join([pat]*5)
    cont2 = cont*5
    count2 += dynamic_counts(pat2, cont2)
print('Part 1:', count)
print('Part 2:', count2)
end_time = time.time()
print("Executes in", round(end_time-start_time, 3), "seconds") # ~1.75 seconds!

