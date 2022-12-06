#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:05:24 2022

@author: stepianno
"""

with open('elf_code.txt') as f:
    code = f.read()
    
string = ''
a = True
for i in range(len(code)):
    while code[i] in string:
        string = string[1:]
    string += code[i]
    if len(string) == 4 and a:
        print('Part 1:', i+1)
        a = False
    if len(string) == 14:
        print('Part 2:', i+1)
        break