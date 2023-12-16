#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:45:30 2023

@author: stepianno
"""

import numpy as np
with open("aoc_14_input.txt") as f:
  data = f.read()
data = np.array([list(x.strip()) for x in data.strip().splitlines()])

spins = []
for t in range(1000000000):
  flag = False
  north = np.copy(data)
  np.place(north, north == 'O', '.')
  for i in range(data.shape[1]):
    s = 0
    squares = np.append(np.where(data[:,i] == '#')[0], data.shape[0])
    for e in squares:
      char, val = np.unique(data[s:e,i], return_counts=True)
      rocks = val[np.where(char == 'O')]
      rocks = rocks[0] if len(rocks) else 0
      locs = np.where(north[s:e,i] == '.')[0]
      if len(locs):
        for n in range(rocks):
          north[s+locs[n], i] = 'O'
      s = e
  if t == 0:
    weight = 0
    for row in range(data.shape[0]):
      rocks = len(np.where(north[row] == 'O')[0])
      weight += rocks * (data.shape[0] - row)
    print('Part 1:', weight)      
  data = np.copy(np.rot90(north, axes=(1,0)))
  if t%4 == 3:
    for i, spin in enumerate(spins, 1):
      if np.array_equal(data, spin):
        around = len(spin) - i
        start = len(spin) + 1
        flag = True
        break
    spins.append(data)
  if flag:
    break
remaining = 1000000000 - start
remainder = remaining % around
north = spins[i+remainder]
weight = 0
for row in range(data.shape[0]):
  rocks = len(np.where(north[row] == 'O')[0])
  weight += rocks * (data.shape[0] - row)
print('Part 2:', weight)