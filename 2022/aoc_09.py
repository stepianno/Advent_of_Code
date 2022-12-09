#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:07:48 2022

@author: stepianno
"""

with open('rope.txt') as f:
    data = [line.strip() for line in f.readlines()]

direction = {
        'D': 1j,
        'R': 1,
        'U': -1j,
        'L': -1
    }
head, tail = 0, 0
portions = [0, 0, 0, 0, 0, 0, 0, 0]
tail_pos = [0]
t9_pos = [0]
for line in data:
    d, n = line.split(' ')
    n = int(n)
    for _ in range(n):
        head += direction[d]
        if abs(head.real - tail.real) > 1:
            tail = tail.real + direction[d] + head.imag*1j
            tail_pos.append(tail)
        elif abs(head.imag - tail.imag) > 1:
            tail = tail.imag*1j + direction[d] + head.real
            tail_pos.append(tail)
        for i in range(len(portions)):
            if i == 0:
                ahead = tail
            else:
                ahead = portions[i-1]
            t = portions[i]
            if abs(ahead.real - t.real) > 1 and abs(ahead.imag - t.imag) > 1:
                real_way = (ahead.real - t.real)/abs(ahead.real - t.real)
                imag_way = (ahead.imag - t.imag)/abs(ahead.imag - t.imag)*1j
                t += real_way + imag_way
            elif abs(ahead.real - t.real) > 1:
                way = (ahead.real - t.real)/abs(ahead.real - t.real)
                t = t.real + way + ahead.imag*1j
            elif abs(ahead.imag - t.imag) > 1:
                way = (ahead.imag - t.imag)/abs(ahead.imag - t.imag)*1j
                t = t.imag*1j + way + ahead.real
            portions[i] = t
            if i == len(portions) - 1:
                t9_pos.append(t)
print('Part 1:', len(set(tail_pos)))
print('Part 2:', len(set(t9_pos)))