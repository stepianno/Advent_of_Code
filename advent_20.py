#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:10:32 2020

@author: stepianno
"""

import numpy as np
import re
from collections import defaultdict

with open('tiles.txt') as f:
    content = f.read()
tiles = content.split('\n\n')
tile_dict = {}
for tile in tiles:
    if not tile:
        continue
    num = int(re.search('\d+', tile).group())
    part = np.array([list(row) for row in tile.splitlines()[1:]])
    top = part[0]
    bot = part[-1]
    left = part[:,0]
    right = part[:,-1]
    whole = part
    tile_dict[num] = {'top':top,'bot':bot,'left':left,'right':right,'whole':whole}
    
match_dict = defaultdict(dict)
sides = ['top','bot','left','right']
for p_tile, p_dict in tile_dict.items():
    for t_tile, t_dict in tile_dict.items():
        if p_tile == t_tile:
            continue
        for p_side in sides:
            for t_side in sides:
                if np.array_equal(p_dict[p_side], t_dict[t_side]):
                    match_dict[p_tile][p_side] = (t_tile,t_side)
                    break
                elif np.array_equal(p_dict[p_side], t_dict[t_side][::-1]):
                    match_dict[p_tile][p_side] = (t_tile,t_side)
                    break

prod = 1
top_left = 0
for k, v in match_dict.items():
    if len(v)==2:
        prod *= k
        check = 0
        for side in v.keys():
            if side == 'right':
                check+=1
            elif side == 'bot':
                check+=1
        if check==2:
            top_left = k
print('part a:',prod)

rotates = {'left': (0,'right'), 'top':(1,'bot'), 'right':(2,'left'), 'bot':(3,'top') }
def make_row(tile, k=0, side='right', match=[], reverse=False):
    grid = np.rot90(tile_dict[tile]['whole'],k=k)
    if reverse:
        grid = grid[:,::-1]
        if side not in match_dict[tile].keys():
            side = rotates[side][1]
    if len(match):
        if not np.array_equal(match, grid[:,0]):
            grid = grid[::-1]
    if side not in match_dict[tile].keys():
        return grid
    next_tile, close_side = match_dict[tile][side]
    next_k, far_side = rotates[close_side]
    return np.hstack((grid, make_row(next_tile,k=next_k,side=far_side, match=grid[:,-1])))

to_rows = {'bot':'right', 'right':'top','top':'left', 'left':'bot'}
rotates_col = {'top':(0,'bot'), 'right':(1,'left'), 'bot':(2,'top'), 'left':(3,'right')}
def make_image(tile, k=0, side='bot', match=[]):
    grid = np.rot90(tile_dict[tile]['whole'],k=k)
    reverse = False
    if len(match):
        if not np.array_equal(match, grid[0]):
            reverse = True
            grid = grid[:,::-1]
    row = make_row(tile, k=k, side=to_rows[side], reverse=reverse)
    if side not in match_dict[tile].keys():
        return row
    next_tile, close_side = match_dict[tile][side]
    next_k, far_side = rotates_col[close_side]
    return np.vstack((row, make_image(next_tile,k=next_k,side=far_side, match=grid[-1])))

image = make_image(top_left)
i=119
j=110
while j >= 0:
    image = np.delete(image, i, 0)
    image = np.delete(image, i, 1)
    image = np.delete(image, j, 0)
    image = np.delete(image, j, 1)
    i -=10
    j -= 10

monster = [(0,0),(1,1),(1,4),(0,5),(0,6),(1,7),(1,10),(0,11),(0,12),(1,13),
           (1,16),(0,17),(0,18),(-1,18),(0,19)]
def is_monster(grid,x,y):
    for i,j in monster:
        try:
            if grid[x+i,y+j] != '#':
                return 0
            
        except:
            return 0
    return 1

monsters = []
for k in range(4):
    count = 0
    image_copy = np.rot90(image, k=k)
    for x in range(len(image)):
        for y in range(len(image[0])):
            count += is_monster(image_copy,x,y)
    monsters.append(count)
    
    count = 0
    image_copy = image_copy[::-1]
    for x in range(len(image)):
        for y in range(len(image[0])):
            count += is_monster(image_copy,x,y)
    monsters.append(count)

print('part b:', np.count_nonzero(image=='#') - len(monster)*max(monsters))


