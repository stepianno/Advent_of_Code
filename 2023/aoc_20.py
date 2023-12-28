#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:42:19 2023

@author: stepianno
"""

import math
with open("aoc_20_input.txt") as f:
  data = f.read()
mods = {}
cons = []
for mod in data.strip().splitlines():
  mod = mod.strip()
  m, o = mod.split(' -> ')
  o = o.split(', ')
  k = ''
  if m != 'broadcaster':
    k = m[0]
    m = m[1:]
  mods[m] = {'out': o, 'type': k}
  if k == '&':
    mods[m]['states'] = {}
    mods[m]['state'] = False
    cons.append(m)
    # for s in o:
    #   mods[m]['state'][s] = False
  else:
    mods[m]['state'] = False
for k, v in mods.items():
  for n in v['out']:
    if n in cons:
      mods[n]['states'][k] = False
low = high = 0
final = [m for m in mods if 'rx' in mods[m]['out']][0]
vals = mods[final]['states'].keys()
val_dict = {val: float('inf') for val in vals}
i = 0
while any([val == float('inf') for val in val_dict.values()]):
  pulses = [('button', 'broadcaster', False)]
  i += 1
  if i == 1000:
    print('Part 1:', low*high)
  while len(pulses):
    origin, mod, p = pulses.pop(0)
    # print(origin, p, '->', mod)
    if p:
      high += 1
    else:
      low += 1
    if mod == 'rx':
      if not p:
        print(i)
        break
      continue
    if mods[mod]['type'] == '%':
      if p:
        continue
      mods[mod]['state'] = not mods[mod]['state']
    elif mods[mod]['type'] == '&':
      mods[mod]['states'][origin] = p
      if all(mods[mod]['states'].values()):
        mods[mod]['state'] = False
      else:
        mods[mod]['state'] = True
        if mod in vals:
          val_dict[mod] = min(val_dict[mod], i)
    for o in mods[mod]['out']:
        pulse = (mod, o, mods[mod]['state'])
        pulses.append(pulse)
print('Part 2:', math.lcm(*[int(x) for x in val_dict.values()]))