#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 23:03:09 2022

@author: stepianno
"""

with open('rucksack.txt') as f:
    bags = [x.strip() for x in f.readlines()]

points = 0

for bag in bags:
    l = len(bag)//2
    c1 = bag[:l]
    c2 = bag[l:]
    for char in c1:
        if char in c2:
            if char == char.upper():
                points += ord(char) - 38
            else:
                points += ord(char) - 96
            break
print('Part 1:', points)

points = 0
for i in range(0, len(bags), 3):
    chars = []
    for char in bags[i]:
        if char in bags[i+1]:
            chars.append(char)
    for char in chars:
        if char in bags[i+2]:
            if char == char.upper():
                points += ord(char) - 38
            else:
                points += ord(char) - 96
            break
print('Part 2:', points)