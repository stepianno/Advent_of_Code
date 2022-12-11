#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 03:06:21 2022

@author: stepianno
"""
import re
import math
with open('monkeys.txt') as f:
    data = f.read().split('\n\n')

monkey_dict = {}
for i in range(len(data)):
    _, start, op, test, true, false = data[i].splitlines()
    start = start.split(': ')[1]
    start = [int(x) for x in start.split(', ')]
    op = re.search('old [+*] (\d+|old)', op).group()
    test = re.search('\d+', test).group()
    true = re.search('\d+', true).group()
    false = re.search('\d+', false).group()
    monkey_dict[i] = {
                'start': start,
                'op': op,
                'test': int(test),
                'true': int(true),
                'false': int(false),
                'count': 0
        }
ceil = math.prod([x['test'] for x in monkey_dict.values()])
for _ in range(10000): #20 for part 1
    x = monkey_dict[0]['count']
    for i in range(len(monkey_dict)):
        for j in range(len(monkey_dict[i]['start'])):
            old = monkey_dict[i]['start'].pop(0)
            old = eval(monkey_dict[i]['op'])%ceil
            #old //= 3 #uncomment for part 1
            true, false = monkey_dict[i]['true'], monkey_dict[i]['false']
            if not old % monkey_dict[i]['test']:
                monkey_dict[true]['start'].append(old)
            else:
                monkey_dict[false]['start'].append(old)
            monkey_dict[i]['count'] += 1
counts = [x['count'] for x in monkey_dict.values()]
counts.sort(reverse=True)
print('Part 1|2:', counts[0]*counts[1])   