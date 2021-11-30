#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 23:04:52 2020

@author: stepianno
"""
import re
import numpy as np

with open('bus.txt') as f:
    content = f.read()
time = int(content.splitlines()[0])
buses = [int(bus) for bus in re.findall('\d+', content.splitlines()[1])]

wait_times = []
for bus in buses:
    wait = bus - time%bus
    wait_times.append(wait)

next_bus = buses[np.argmin(wait_times)]
print(next_bus * min(wait_times))

bus_line = content.splitlines()[1].split(',')

parts = ['t%'+bus_line[0]+'==0']
for i, bus in enumerate(bus_line[1:],1):
    if bus=='x':
        continue
    else:
        while i > int(bus):
            i -= int(bus)
        parts.append(f"{bus}-t%{bus}=={i}")

t = buses[0]
ups = buses[0]
for part in parts[1:]:
    inc = []
    while len(inc)<2:
        if eval(part.replace('t',str(t))):
            inc.append(t)
        t += ups
    t = inc[0]
    ups = inc[1] - inc[0]
print(t)