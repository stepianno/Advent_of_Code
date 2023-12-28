#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:33:56 2023

@author: stepianno
"""

import re
with open("aoc_19_input.txt") as f:
  data = f.read()
inst, parts = data.split('\n\n')
parts = [row.strip()[1:-1].split(',') for row in parts.strip().splitlines()]
part_dicts = []
for part in parts:
  ob = {}
  for x in part:
    k, v = x.split('=')
    ob[k] = v
  part_dicts.append(ob)
rule_dict = {}
for line in inst.strip().splitlines():
  line = line.strip().replace('{', ',').replace('}', '')
  k, *rules = line.split(',')
  if not len(rules):
    print(line)
  rule_dict[k] = []
  for rule in rules[:-1]:
    x = rule[0]
    op = rule[1]
    n = re.search('\d+', rule[2:]).group()
    w = re.search('[A-Za-z]+', rule[3:]).group()
    rule_dict[k].append((x, op, n, w))
  rule_dict[k].append(rules[-1])
count = 0
for part in part_dicts:
  c = 'in'
  while c not in 'AR':
    rules = rule_dict[c]
    flag = True
    for l, op, n, w in rules[:-1]:
      if eval(part[l] + op + n):
        c = w
        flag = False
        break
    if flag:
      c = rules[-1]
    if c == 'A':
      count += sum([int(x) for x in part.values()])
print('Part 1:', count)

deck = [{'x': (1,4000), 'm': (1,4000), 'a':(1,4000), 's': (1,4000), 'at': 'in', 'step': 0}]
passed = []
while len(deck):
  combo = deck.pop(0)
  rule = rule_dict[combo['at']][combo['step']]
  if type(rule) == str:
    if rule == 'A':
      passed.append(combo)
    elif rule != 'R':
      combo['at'] = rule
      combo['step'] = 0
      deck.append(combo)
  else:
    good = combo.copy()
    bad = combo.copy()
    key = rule[0]
    op = rule[1]
    at = rule[3]
    if op == '>':
      point = int(rule[2]) + 1
      if point <= good[key][1]:
        good[key] = (point, good[key][1])
        if at == 'A':
          passed.append(good)
        elif at != 'R':
          good['at'] = at
          good['step'] = 0
          deck.append(good)
      if point > bad[key][0]:
        bad[key] = (bad[key][0], point-1)
        bad['step'] += 1
        deck.append(bad)
    else:
      point = int(rule[2])
      if point > good[key][0]:
        good[key] = (good[key][0], point - 1)
        if at == 'A':
          passed.append(good)
        elif at != 'R':
          good['at'] = at
          good['step'] = 0
          deck.append(good)
      if point < bad[key][1]:
        bad[key] = (point, bad[key][1])
        bad['step'] += 1
        deck.append(bad)
combos = 0
for d in passed:
  p = 1
  for k in ['x', 'm', 'a', 's']:
    p *= d[k][1] - d[k][0] + 1
  combos += p
print('Part 2:', combos)