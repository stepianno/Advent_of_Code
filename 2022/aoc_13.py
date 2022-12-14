#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:18:07 2022

@author: stepianno
"""

with open('list_pairs.txt') as f:
    data = f.read().split('\n\n')
    data = [pair.split('\n') for pair in data]

def comp(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return False
        if type(left[i]) == int and type(right[i]) == list:
            left[i] = [left[i]]
        if type(right[i]) == int and type(left[i]) == list:
            right[i] = [right[i]]
        if type(left[i]) == int:
            if left[i] > right[i]:
                return False
            elif left[i] < right[i]:
                return True
            else:
                continue
        else:
            depth = comp(left[i], right[i])
            if depth == 'f':
                continue
            else:
                return depth
    if len(left) < len(right):
        return True
    else:
        return 'f'

ind_sum = 0
top = 1
mid = 2
for i, pair in enumerate(data, 1):
    left = eval(pair[0])
    right = eval(pair[1])
    if comp(left, right):
        ind_sum += i
    for b in [left, right]:
        top += comp(b, [[2]])
        mid += comp(b, [[6]])
print('Part 1:', ind_sum)
print('Part 2:', top*mid)