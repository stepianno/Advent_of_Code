#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 23:07:53 2020

@author: stepianno
"""

card = 17115212
door = 3667832

def loop_size(key):
    value = 1
    subject = 7
    n = 0
    while value != key:
        value *= subject
        value = value % 20201227
        n += 1
    return n

card_loop = loop_size(card)
door_loop = loop_size(door)

def encrypt(subject, loop):
    value = 1
    for _ in range(loop):
        value *= subject
        value = value % 20201227
    return value

print(encrypt(card, door_loop))
print(encrypt(door, card_loop))