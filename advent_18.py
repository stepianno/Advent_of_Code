#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:18:05 2020

@author: stepianno
"""
import re

with open('math.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

def no_parans(line):
    while not line.isdigit():
        solve = re.match('\d+ [+*] \d+', line).group()
        line = line.replace(solve, str(eval(solve)), 1)
    return line

def no_parans_adv(line):
    while not line.isdigit():
        solve = re.search('\d+ [+] \d+', line)
        if solve:
            solve = solve.group()
        else:
            solve = re.match('\d+ [*] \d+', line).group()
        line = line.replace(solve, str(eval(solve)), 1)
    return line


def do_math(line, adv=False):
    i = 0
    s, e = 0, 0
    while '(' in line:
        if line[i] == '(':
            s = i
        elif line[i] == ')':
            e = i
            if adv:
                try:
                    line = line[:s] + no_parans_adv(line[s+1:e]) + line[e+1:]
                except:
                    line = line[:s] + no_parans_adv(line[s+1:e])
                i = -1
            else:
                try:
                    line = line[:s] + no_parans(line[s+1:e]) + line[e+1:]
                except:
                    line = line[:s] + no_parans(line[s+1:e])
                i = -1
        i+=1
    return int(no_parans(line)) if not adv else int(no_parans_adv(line))
    
sum_ = 0
for line in content:
    sum_ += do_math(line)
print('part a:',sum_)

sum_ = 0 
for line in content:
    sum_ += do_math(line, True)
print('part b:',sum_)