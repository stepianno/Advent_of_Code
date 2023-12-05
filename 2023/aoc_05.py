#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:50:32 2023

@author: stepianno
"""

with open('aoc_05_input.txt') as f:
    data = f.read()
seeds, *maps = data.strip().split('\n\n')
seeds = [int(x) for x in seeds[7:].split()]
maps = [[[int(x) for x in line.split()] for line in mapp.split('\n')[1:]] for mapp in maps]
min_loc = float('inf')
for seed in seeds:
    for mapp in maps:
        for line in mapp:
            top = line[1] + line[2] - 1
            if seed >= line[1] and seed <= top:
                dif = seed - line[1]
                seed = line[0] + dif
                break
    if seed < min_loc:
        min_loc = seed
print('Part 1:', min_loc)
min_loc = float('inf')
for seed, r in zip(seeds[::2], seeds[1::2]):
    spread = [(seed, seed+r-1)]
    for mapp in maps:
        new_spread = []
        for a, b in spread:
            flag = False
            for line in mapp:
                top = line[1] + line[2] - 1
                if a >= line[1] and b <= top:
                    dif1 = a - line[1]
                    x = line[0] + dif1
                    dif2 = b - line[1]
                    y = line[0] + dif2
                    new_spread.append((x,y))
                    flag = True
                    break
                elif a < line[1] and b > top:
                    new_spread.append((line[0], line[0]+line[2]-1))
                    spread.append((a, line[1]-1))
                    spread.append((top+1, b))
                    flag = True
                    break
                elif a >= line[1] and a <=top:
                    dif1 = a - line[1]
                    x = line[0] + dif1
                    new_spread.append((x, line[0]+line[2]-1))
                    spread.append((top+1, b))
                    flag = True
                    break
                elif b >= line[1] and b <= top:
                    dif2 = b - line[1]
                    y = line[0] + dif2
                    new_spread.append((line[0],y))
                    spread.append((a, line[1]-1))
                    flag = True
                    break
            if not flag:
                new_spread.append((a,b))
        spread = new_spread
    min_seed = min([x[0] for x in spread])
    if min_seed < min_loc:
        min_loc = min_seed
print('Part 2:', min_loc)
                    
                    
                    
                    
                    