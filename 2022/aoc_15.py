#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:50:07 2022

@author: stepianno
"""
import re
with open('beacons.txt') as f:
    data = [[[int(y) for y in re.findall('-?\d+', n)] for n in x.split(': ')] for x in f.readlines()]
row = 2000000
beacons_1 = set([x[1][0] for x in data if x[1][1] == row])
non_beacons_1 = []
for sensor, beacon in data:
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    remainder = distance - abs(sensor[1] - row)
    if remainder > 0:
        low = sensor[0]-remainder
        high = sensor[0]+remainder
        flag = True
        for i in range(len(non_beacons_1)):
            if high <= non_beacons_1[i][1] and high >= non_beacons_1[i][0]:
                non_beacons_1[i][0] = min(low, non_beacons_1[i][0])
                flag = False
                break
            elif low <= non_beacons_1[i][1] and low >= non_beacons_1[i][0]:
                non_beacons_1[i][1] = max(high, non_beacons_1[i][1])
                flag = False
                break
            elif low < non_beacons_1[i][0] and high > non_beacons_1[i][1]:
                non_beacons_1[i] = [low, high]
                flag = False
                break
            elif low > non_beacons_1[i][0] and high < non_beacons_1[i][1]:
                flag = False
                break
        if flag:
            non_beacons_1.append([low, high])
while True:
    non_copy = non_beacons_1.copy()
    for i in range(1, len(non_beacons_1)):
        high = non_beacons_1[0][1]
        low = non_beacons_1[0][0]
        if high <= non_beacons_1[i][1] and high >= non_beacons_1[i][0]:
           non_beacons_1[0][1] = non_beacons_1[i][1]
           non_beacons_1[0][0] = min(non_beacons_1[0][0], non_beacons_1[i][0])
           non_beacons_1.pop(i)
           break
        if low <= non_beacons_1[i][1] and low >= non_beacons_1[i][0]:
           non_beacons_1[0][0] = non_beacons_1[i][0]
           non_beacons_1[0][1] = max(non_beacons_1[0][1], non_beacons_1[i][1])
           non_beacons_1.pop(i)
           break
    if non_beacons_1 == non_copy:
        break
one = 0
for low, high in non_beacons_1:
    count = high - low + 1
    for beacon in beacons_1:
        if beacon >= low and beacon <= high:
            count -= 1
    one += count
print('Part 1:', one)

diamonds = []
size = 4000000
for sensor, beacon in data:
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    diamonds.append((sensor[0], sensor[1], distance))
    
def inside(i, j, r, x, y):
    distance = abs(i - x) + abs(j - y)
    return distance <= r
flag = False
for i, diamond in enumerate(diamonds):
    x_coord, y_coord, distance = diamond
    y = y_coord - distance - 1
    x = x_coord
    a = 1
    b = 1
    for _ in range((distance + 1)*4):
        if x >= 0 and x <= size and y >= 0 and y <= size:
            flag = True
            for other in diamonds:
                other_x, other_y, r = other
                if inside(other_x, other_y, r, x, y):
                    flag = False
                    break
        if flag:
            print('Part 2:', x*size + y)
            break
        x += a
        y += b
        if x == x_coord + distance + 1:
            a = -1
        if y == y_coord + distance + 1:
            b = -1
        if x == x_coord - distance - 1:
            a = 1
    if flag:
        break
            