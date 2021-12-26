#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:56:58 2021

@author: stepianno
"""
from itertools import combinations_with_replacement
from collections import Counter
p1 = p2 = 0
s1 = 2
s2 = 1
die = 0
first = True
while p1 < 1000 and p2 < 1000:
    die += 3
    move = (die*3-3)%10
    if first:
        s1 = (s1+move)%10
        if not s1:
            p1 += 10
        else:
            p1 += s1
    else:
        s2 = (s2+move)%10
        if not s2:
            p2 += 10
        else:
            p2 += s2
    first = not first
print('part a:', min(p1,p2)*die)

ways = combinations_with_replacement([1,2,3], 3)
paths = Counter([sum(way) for way in ways])
start = (2,1,True,0,0)
dim_cache = {}
def dirac(s1, s2, first=True, p=0):
    turn = (s1,s2,first,p)
    if turn in dim_cache:
        return dim_cache[turn]
    if p.real >= 21:
        return 1
    elif p.imag >= 21:
        return 1j
    w = 0
    for a in range(1,4):
        for b in range(1,4):
            for c in range(1,4):
                k = a+b+c
                if first:
                    s1n = (s1 + k)%10
                    if not s1n:
                        pn = p + 10
                    else:
                        pn = p + s1n
                    w += dirac(s1n,s2,False,pn)
                else:
                    s2n = (s2 + k)%10
                    if not s2n:
                        pn = p + 10j
                    else:
                        pn = p + (s2n*1j)
                    w += dirac(s1,s2n,True,pn)
    dim_cache[turn] = w
    return dim_cache[turn]

dirac(2,1)
p1 = int(dim_cache[(2,1,True,0)].real)
p2 = int(dim_cache[(2,1,True,0)].imag)
print('part b:', max(p1,p2))






