#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 22:55:45 2021

@author: stepianno
"""
from collections import defaultdict
with open('caves.txt') as f:
    caves = [line.strip().split('-') for line in f.readlines()]

maps = defaultdict(list)
for a, b in caves:
    maps[a].append(b)
    maps[b].append(a)
def spalunking(cave, path=''):
    if cave.lower() == cave:
        if cave in path:
            return 0
        path += cave + ','
    if cave == 'end':
        return 1
    routes = 0
    for c in maps[cave]:
        routes += spalunking(c, path)
    return routes
print('part a:', spalunking('start'))

def more_spalunking(cave, path='', flag=False):
    if cave.lower() == cave:
        if (cave in path and flag) or (cave == 'start' and cave in path):
            return 0
        elif cave in path:
            flag = True
        path += cave + ','
    if cave == 'end':
        return 1
    routes = 0
    for c in maps[cave]:
        routes += more_spalunking(c, path, flag)
    return routes
print('part b:', more_spalunking('start'))