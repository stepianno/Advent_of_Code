#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:06:33 2022

@author: stepianno
"""

with open('calories.txt') as f:
    data = f.read()
data = [[int(y) if y else 0 for y in x.split('\n')] for x in data.split('\n\n')]
print(max([sum(d) for d in data]))
print(sum(sorted([sum(d) for d in data], reverse=True)[:3]))