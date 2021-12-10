#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 00:58:27 2021

@author: stepianno
"""

with open('brackets.txt') as f:
    content = f.readlines()
content = [line.strip() for line in content]
brak_check = {')': '(', ']': '[', '>': '<', '}': '{'}
wrongs = []
wrongs_dict = {')': 3, ']': 57, '>': 25137, '}': 1197}
rights_dict = {'(': 1, '[': 2, '{': 3, '<': 4}
right_counts = []
for line in content:
    rights = []
    flag = True
    for b in line:
        if b in '{<([':
            rights.append(b)
        else:
            if rights[-1] == brak_check[b]:
                rights.pop()
            else:
                wrongs.append(b)
                flag = False
                break
    if flag:
        rights.reverse()
        right_count = 0
        for r in rights:
            right_count *= 5
            right_count += rights_dict[r]
        right_counts.append(right_count)
wrong_count = 0
for w in wrongs:
    wrong_count += wrongs_dict[w]
print('part a:', wrong_count)
ind = len(right_counts) // 2
right_counts.sort()
print('part b:', right_counts[ind])