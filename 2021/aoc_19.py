#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:29:43 2021

@author: stepianno
"""
from collections import defaultdict
from math import sqrt
with open('beacons.txt') as f:
    scans = f.read()
scans = scans.split('\n\n')
scans = [[[int(x) for x in y.split(',')] for y in scan.splitlines()[1:]] for scan in scans]

probe_dists = defaultdict(list)
for n, scan in enumerate(scans):
    for i, probe in enumerate(scan):
        a,b,c = probe
        for j, oprobe in enumerate(scan):
            x,y,z = oprobe
            if i==j:
                continue
            dist = sqrt((a-x)**2 + (b-y)**2+ (c-z)**2)
            probe_dists[str(n)+'_'+str(i)].append(dist)
same_probes = {}
for i in range(len(scans)):
    same_probes[str(i)] = defaultdict(list)
for probe_a, dists_a in probe_dists.items():
    for probe_b, dists_b in probe_dists.items():
        if probe_a.split('_')[0] == probe_b.split('_')[0]:
            continue
        sames = set(dists_a) & set(dists_b)
        if len(sames) >= 11:
            same_probes[probe_a.split('_')[0]][probe_a].append(probe_b)
sensor_dicts = {'0': (0,0,0,1,1,1,0,1,2)}
confs = [
        (1,1,1),
        (-1,1,1),
        (1,-1,1),
        (1,1,-1),
        (-1,-1,1),
        (-1,1,-1),
        (1,-1,-1),
        (-1,-1,-1)
    ]
orients = [
        (0,1,2),
        (1,0,2),
        (1,2,0),
        (2,1,0),
        (0,2,1),
        (2,0,1)
    ]

while len(sensor_dicts) < len(scans):
    for sensor, probe_matches in same_probes.items():
        if sensor not in sensor_dicts:
            continue
        checks = {}
        for i in range(len(scans)):
            checks[str(i)] = defaultdict(int)
        for probe, matches in probe_matches.items():
            index = int(probe.split('_')[1])
            abc = scans[int(sensor)][index]
            a = abc[sensor_dicts[sensor][6]]
            b = abc[sensor_dicts[sensor][7]]
            c = abc[sensor_dicts[sensor][8]]
            a = (a*sensor_dicts[sensor][3])+sensor_dicts[sensor][0]
            b = (b*sensor_dicts[sensor][4])+sensor_dicts[sensor][1]
            c = (c*sensor_dicts[sensor][5])+sensor_dicts[sensor][2]
            for match in matches:
                search_sensor = match.split('_')[0]
                match_ind = int(match.split('_')[1])
                xyz = scans[int(search_sensor)][match_ind]
                for o1,o2,o3 in orients:
                    x = xyz[o1]
                    y = xyz[o2]
                    z = xyz[o3]
                    for d1,d2,d3 in confs:
                        v1 = a - x*d1
                        v2 = b - y*d2
                        v3 = c - z*d3
                        checks[search_sensor][(v1,v2,v3,d1,d2,d3,o1,o2,o3)] += 1
        for sensor, check in checks.items():
            if not check or max(check.values()) < 5:
                continue
            sensor_vals = max(check, key=lambda x: check[x])
            sensor_dicts[sensor] = sensor_vals
probes = []
for n, scan in enumerate(scans):
    for abc in scan:
        a = abc[sensor_dicts[str(n)][6]]
        b = abc[sensor_dicts[str(n)][7]]
        c = abc[sensor_dicts[str(n)][8]]
        a = (a*sensor_dicts[str(n)][3])+sensor_dicts[str(n)][0]
        b = (b*sensor_dicts[str(n)][4])+sensor_dicts[str(n)][1]
        c = (c*sensor_dicts[str(n)][5])+sensor_dicts[str(n)][2]
        if (a,b,c) not in probes:
            probes.append((a,b,c))
print('part a:', len(probes))
max_dist = 0
for x1,y1,z1, *_ in sensor_dicts.values():
    for x2,y2,z2, *_ in sensor_dicts.values():
        man_d = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
        if man_d > max_dist:
            max_dist = man_d
print('part b:', max_dist)






