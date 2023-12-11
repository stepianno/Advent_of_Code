#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 22:56:25 2023

@author: stepianno
"""
import numpy as np
with open('aoc_11_input.txt') as f:
    data = f.read()
data = np.array([list(row.strip()) for row in data.strip().splitlines()])
#h_fill = np.array(['.']*data.shape[0]).reshape((data.shape[0], 1))
vs = []
hs = []
for i in range(len(data[0])):
    if len(np.unique(data[:,i])) == 1:
        hs.append(i)
for i in range(len(data)):
    if len(np.unique(data[i,:])) == 1:
        vs.append(i)
gals = np.where(data == '#')
gals = [a+b*1j for a,b in zip(gals[0], gals[1])]
ds = 0
d2s = 0
vs = np.array(vs)
hs = np.array(hs)
for i in range(len(gals)):
    for j in range(i+1, len(gals)):
        by, ly = max(gals[i].real, gals[j].real), min(gals[i].real, gals[j].real)
        bx, lx = max(gals[i].imag, gals[j].imag), min(gals[i].imag, gals[j].imag)
        h_adds = len(np.where((hs < bx) & (hs > lx))[0])
        v_adds = len(np.where((vs < by) & (vs > ly))[0])
        d = (by+v_adds - ly) + (bx+h_adds - lx)
        d2 = (by+(v_adds*999999) - ly) + (bx+(h_adds*999999) - lx)
        ds += d
        d2s += d2
print('Part 1:', ds)
print('Part 2:', d2s)