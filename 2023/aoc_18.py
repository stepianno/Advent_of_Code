#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:55:28 2023

@author: stepianno
"""

data = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''
with open("aoc_18_input.txt") as f:
  data = f.read()
data = [[x for x in row.strip().split()] for row in data.strip().splitlines()]
dir_dict = {
        'R': 1j,
        'L': -1j,
        'U': -1,
        'D': 1,
        '0': 1j,
        '1': 1,
        '2': -1j,
        '3': -1
    }
points = [0]
points2 = [0]
for d, n, c in data:
    n = int(n)
    d = dir_dict[d]
    m = d*n
    points.append(m+points[-1])
    n2 = int('0x'+c[2:7], 0)
    d2 = dir_dict[c[-2]]
    m2 = d2*n2
    points2.append(m2+points2[-1])
    
'''shift = (min([n.real for n in points]) + min([n.imag for n in points])*1j)*-1
points = [n+shift for n in points]'''
shoelace = 0
boundary = 0
for p1, p2 in zip(points, points[1:] + [points[0]]):
    shoelace += (p2.imag + p1.imag)*(p2.real - p1.real)
    boundary += abs(p2-p1)
print(0.5*(shoelace) + 0.5*boundary + 1)
shoelace = 0
boundary = 0
for p1, p2 in zip(points2, points2[1:] + [points2[0]]):
    shoelace += (p2.imag + p1.imag)*(p2.real - p1.real)
    boundary += abs(p2-p1)
print(0.5*(shoelace) + 0.5*boundary + 1)
