#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 23:05:18 2020

@author: stepianno
"""

import numpy as np

with open('seats.txt') as f:
    content = f.readlines()
content = np.array([list('.'+x.strip()+'.') for x in content])

filler = np.repeat('.', content.shape[1])
seats = np.vstack((filler,content,filler))
seats2 = seats.copy()

look_around = [(-1,-1),(-1,0),(-1,1),(0,1),(1,0),(1,1),(1,-1),(0,-1)]

def seat_change(seats):
    new_seats = seats.copy()
    for i in range(1,seats.shape[0]-1):
        for j in range(1,seats.shape[1]-1):
            if seats[i,j] == '.':
                continue
            count = 0
            for x,y in look_around:
                if seats[i+x,j+y] == '#':
                    count += 1
            if seats[i,j] == 'L' and count == 0:
                new_seats[i,j] = '#'
            elif seats[i,j] == '#' and count >= 4:
                new_seats[i,j] = 'L'
    return new_seats

while True:
    old_seats = seats.copy()
    seats = seat_change(seats)
    if np.array_equal(seats, old_seats):
        break
    
print(np.count_nonzero(seats == '#'))

def seat_change2(seats):
    new_seats = seats.copy()
    for i in range(1,seats.shape[0]-1):
        for j in range(1,seats.shape[1]-1):
            if seats[i,j] == '.':
                continue
            count = 0
            for x,y in look_around:
                xx = x
                yy = y
                while seats[i+x,j+y] == '.':
                    if i+x==0 or i+x==seats.shape[0]-1 or j+y==0 or j+y==seats.shape[1]-1:
                        break
                    x += xx
                    y += yy
                if seats[i+x,j+y] == '#':
                    count += 1
            if seats[i,j] == 'L' and count == 0:
                new_seats[i,j] = '#'
            elif seats[i,j] == '#' and count >= 5:
                new_seats[i,j] = 'L'
    return new_seats

while True:
    old_seats = seats2.copy()
    seats2 = seat_change2(seats2)
    if np.array_equal(seats2, old_seats):
        break
    
print(np.count_nonzero(seats2 == '#'))