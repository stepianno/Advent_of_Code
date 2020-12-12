#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:03:21 2020

@author: stepianno
"""

with open('directions.txt') as f:
    content = f.readlines()
content = [x.strip()for x in content]

#content = ['F10','N3','F7','R90','F11']

forward = 'E'
distances = {'E': 0, 'N': 0, 'W': 0, 'S': 0}
right_90 = {'E': 'S', 'S': 'W', 'W':'N', 'N':'E'}
left_90 = {'E': 'N', 'N':'W','W':'S','S':'E'}
one_eighty = {'E':'W','W':'E','N':'S','S':'N'}
for way in content:
    direction = way[0]
    amount = int(way[1:])
    if direction == 'F':
        distances[forward] += amount
    elif (direction == 'R' and amount == 90) or (direction == 'L' and amount == 270):
        forward = right_90[forward]
    elif (direction == 'L' and amount == 90) or (direction == 'R' and amount == 270):
        forward = left_90[forward]
    elif direction == 'R' or direction == 'L':
        forward = one_eighty[forward]
    else:
        distances[direction] += amount
    #print(way, forward, distances)
horizontal = abs(distances['E'] - distances['W'])
vertical = abs(distances['N'] - distances['S'])

print('part 1:',horizontal + vertical)

wayward = {'E':10, 'N':1, 'S':0, 'W':0}
distances = {'E': 0, 'N': 0, 'W': 0, 'S': 0}
right_90 = {'E': 'S', 'S': 'W', 'W':'N', 'N':'E'}
left_90 = {'E': 'N', 'N':'W','W':'S','S':'E'}
one_eighty = {'E':'W','W':'E','N':'S','S':'N'}
for way in content:
    direction = way[0]
    amount = int(way[1:])
    if direction == 'F':
        for k in wayward.keys():
            distances[k] += wayward[k]*amount
    elif (direction == 'R' and amount == 90) or (direction == 'L' and amount == 270):
        fakeward = wayward.copy()
        for k in wayward.keys():
            wayward[k] = fakeward[left_90[k]]
    elif (direction == 'L' and amount == 90) or (direction == 'R' and amount == 270):
        fakeward = wayward.copy()
        for k in wayward.keys():
            wayward[k] = fakeward[right_90[k]]
    elif direction == 'R' or direction == 'L':
        fakeward = wayward.copy()
        for k in wayward.keys():
            wayward[k] = fakeward[one_eighty[k]]
    else:
        if wayward[one_eighty[direction]] == 0:
            wayward[direction] += amount
        elif wayward[one_eighty[direction]] >= amount:
            wayward[one_eighty[direction]] -= amount
        else:
            wayward[direction] = amount - wayward[one_eighty[direction]]
            wayward[one_eighty[direction]] = 0
    
            
horizontal = abs(distances['E'] - distances['W'])
vertical = abs(distances['N'] - distances['S'])

print('part 2:',horizontal + vertical)