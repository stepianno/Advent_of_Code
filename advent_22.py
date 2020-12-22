#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 23:04:30 2020

@author: stepianno
"""

from collections import deque

with open('cards.txt') as f:
    content = f.read()
hand1, hand2 = content.split('\n\n')
hand1 = deque([int(n) for n in hand1.splitlines()[1:]])
hand2 = deque([int(n) for n in hand2.splitlines()[1:]])

hand1r = hand1.copy()
hand2r = hand2.copy()

def combat(hand1, hand2):
    i = 0
    while hand1 and hand2:
        if i==1000:
            return(0,1)
        x = hand1.popleft()
        y = hand2.popleft()
        if x > y:
            hand1.append(x)
            hand1.append(y)
        elif y > x:
            hand2.append(y)
            hand2.append(x)
        i += 1
    winner = hand1 or hand2
    if hand1:
        out = 1
    else:
        out = 2
    return(winner,out)
    
        
winner = combat(hand1, hand2)[0]
score = 0
for i in range(len(winner)):
    score += int(winner[i])*(len(winner)-i)
print('part a:', score)

while hand1r and hand2r:
    x = hand1r.popleft()
    y = hand2r.popleft()
    if x <= len(hand1r) and y <= len(hand2r):
        first = list(hand1r)[:x]
        second = list(hand2r)[:y]
        h = combat(deque(first), deque(second))[1]
        if h == 1:
            hand1r.append(x)
            hand1r.append(y)
        else:
            hand2r.append(y)
            hand2r.append(x)
    else:
        if x > y:
            hand1r.append(x)
            hand1r.append(y)
        elif y > x:
            hand2r.append(y)
            hand2r.append(x)

winner = hand1r or hand2r
score = 0
for i in range(len(winner)):
    score += int(winner[i])*(len(winner)-i)
print('part b:', score)
        
        
        
        
        