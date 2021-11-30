#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:00:14 2020

@author: stepianno
"""
import re

with open('rules.txt') as f:
    content = f.read()
rules, codes = content.split('\n\n')
rule_dict = {}
for rule in rules.splitlines():
    x, y = rule.split(': ')
    if y == '"a"' or y == '"b"':
        y = y.replace('"', '')
    else:
        y = [int(n) if n.isdigit() else n for n in y.split()]
    x = int(x)
    rule_dict[x] = y

codes = [x.strip() for x in codes.splitlines()]

memo = {}
def find_parse(rules, n=0):
    if rules[n] == 'a' or rules[n] == 'b':
        memo[n]=rules[n]
    if n in memo:
        return memo[n]
    string = ''
    if '|' in rules[n]:
        string += '('
        for x in rules[n]:
            if x == '|':
                string += x
            else:
                string += find_parse(rules, x)
        string += ')'
    else:
        for x in rules[n]:
            string += find_parse(rules, x)
    memo[n] = string
    return memo[n]
find_parse(rule_dict)

count = 0
for code in codes:
    if re.search('^'+memo[0]+'$', code):
        count += 1
print('part a:',count)

count = 0
n = 1
while True:
    old = count
    for code in codes:
        if re.search('^'+memo[8]+'+'+memo[42]+'{'+str(n)+'}'+memo[31]+'{'+str(n)+'}$', code):
            count += 1
    if count == old:
        break
    n += 1
    
print('part b:',count)





