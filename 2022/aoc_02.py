#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:03:09 2022

@author: stepianno
"""

with open('rps.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]

points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
game_map = {
        'X': {
                'A': 3,
                'B': 0,
                'C': 6
            },
        'Y': {
                'A': 6,
                'B': 3,
                'C': 0
            },
        'Z': {
                'A': 0,
                'B': 6,
                'C': 3
            }
        }
score = 0
for game in data:
    opp, me = game.split(' ')
    score += points[me]
    score += game_map[me][opp]
print('part 1:', score)

points = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }
game_map = {
        'A': {
                'X': 3,
                'Y': 1,
                'Z': 2
            },
        'B': {
                'X': 1,
                'Y': 2,
                'Z': 3
            },
        'C': {
                'X': 2,
                'Y': 3,
                'Z': 1
            }
        }
score = 0
for game in data:
    opp, me = game.split(' ')
    score += points[me]
    score += game_map[opp][me]
print('part 2:', score)