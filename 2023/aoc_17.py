#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 08:57:26 2023

@author: stepianno
"""
import heapq
data = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''
with open("aoc_17_input.txt") as f:
  data = f.read()
grid = {}
for j, row in enumerate(data.strip().splitlines()):
    for i, n in enumerate(row.strip()):
        grid[j+i*1j] = int(n)
move_dict = {
        'r': [-1, 1],
        'l': [-1, 1],
        'u': [1j, -1j],
        'd': [1j, -1j],
        'f': [1, 1j]
    }
dir_dict = {
        1: 'd',
        -1: 'u',
        1j: 'r',
        -1j: 'l'
    }
def min_path(low, high):
    deck = [(0, 0, 0,'f')]
    cache = set()
    best = float('inf')
    end = [*grid][-1]
    count = 1
    while len(deck):
        heat, c, key, d = heapq.heappop(deck)
        if (key, d) in cache:
            continue
        cache.add((key, d))
        if key == end and heat < best:
            best = heat
        moves = move_dict[d]
        for w in moves:
            direction = dir_dict[w]
            for i in range(low, high+1):
                spot = key + w*i
                if spot in grid:
                    new_heat = heat + sum([grid[key+x*w] for x in range(1,i+1)])
                    heapq.heappush(deck, (new_heat, count, spot, direction))
                    count += 1
    return best
print('Part 1:', min_path(1,3))
print('Part 2:', min_path(4,10))