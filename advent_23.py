#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 23:15:35 2020

@author: stepianno
"""
#My first strategy with a deque was not fast enough for part b, so I shifted to a linked list
from collections import deque

cups = deque([9,1,6,4,3,8,2,7,5])

def turn_deque(cups, n=1):
    for _ in range(n):
        picked = deque()
        current = cups[0]
        cups.rotate(-1)
        for _ in range(3):
            picked.append(cups.popleft())
        k = current - 1
        while k > 0:
            try:
                i = cups.index(k)
                break
            except:
                k -= 1
        if k == 0:
            i = cups.index(max(cups))
        for _ in range(3):
            cups.insert(i+1,picked.pop())
        if _%1000 == 0:
            print(_)
    return cups

done = turn_deque(cups.copy(), 100)
done.rotate(-done.index(1)-1)
print('part a:',''.join([str(x) for x in done if x != 1]))

#This strategy was vastly more efficient!
linked_a = {}
for i, cup in enumerate(cups):
    try:
        linked_a[cup] = cups[i+1]
    except:
        linked_a[cup] = cups[0]
        
def turn_link(cup, linked, n=1):
    min_ = min(linked)
    max_ = max(linked)
    for _ in range(n):
        first = linked[cup]
        second = linked[first]
        third = linked[second]
        fourth = linked[third]
        check = [first,second,third]
        loc = cup-1
        if loc < min_:
            loc = max_
        while loc in check:
            loc -= 1 
            if loc == 0:
                loc = max_
        after = linked[loc]
        linked[cup] = fourth
        linked[loc] = first
        linked[third] = after
        cup = fourth
        if _%1000000 == 0 and _:
            print(round(_/n*100, 2),'%')
    return linked

x = turn_link(cups[0],linked_a,100)
cup = x[1]
string = str(cup)
while cup != 1:
    string += str(x[cup])
    cup = x[cup]
print('part a2.0:',string[:-1])

cups_b = list(cups) + list(range(10,10**6+1))
linked_b = {}
for i, cup in enumerate(cups_b):
    try:
        linked_b[cup] = cups_b[i+1]
    except:
        linked_b[cup] = cups_b[0]

y = turn_link(cups_b[0],linked_b, 10**7)
first = y[1]
second = y[first]
print(first,second,first*second)
