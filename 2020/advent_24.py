#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:15:02 2020

@author: stepianno
"""

with open('hexagons.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


directions = ['e','w','ne','se','nw','sw']
direction_dict = {'e': 2, 'w': -2, 'ne': 1+1j, 'nw': -1+1j, 'se':1-1j, 'sw':-1-1j}

tiles = []
for tile in content:
    i = 0
    directions = []
    while i < len(tile):
        if tile[i] in 'ew':
            directions.append(tile[i])
            i += 1
        else:
            directions.append(tile[i:i+2])
            i += 2
    tiles.append(directions)
    
tile_dict = {}
for tile in tiles:
    loc = 0
    for d in tile:
        loc += direction_dict[d]
    if loc in tile_dict:
        tile_dict[loc] = 0 # 0 for white
    else:
        tile_dict[loc] = 1 # 1 for black

print('part a:',sum(tile_dict.values()))

for i in range(10):
    absent = []
    for tile, color in tile_dict.items():
        for nei in direction_dict.values():
            if tile+nei not in tile_dict:
                absent.append(tile+nei)
    for loc in absent:
        tile_dict[loc] = 0
for i in range(100):
    absent = []
    tile_copy = tile_dict.copy()
    for tile, color in tile_copy.items():
        count = 0
        for nei in direction_dict.values():
            if tile+nei not in tile_dict:
                absent.append(tile+nei)
            else:
                count += tile_copy[tile+nei]
        if color==1: 
            if count > 2 or count==0:
                tile_dict[tile] = 0
        elif color == 0 and count == 2:
            tile_dict[tile] = 1
    for loc in absent:
        tile_dict[loc] = 0
print('part b:',sum(tile_dict.values()))

        

