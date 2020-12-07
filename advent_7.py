#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 00:09:23 2020

@author: stepianno
"""

import re

with open('bags.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

count = 0
with_gold = []
gold_line = []
for i, line in enumerate(content):
    if re.search('\d shiny gold bag', line):
        count += 1
        color = re.search('^[a-z]+ [a-z]+ bag', line).group()
        with_gold.append(color)
        gold_line.append(i)
for bag in with_gold:
    for i, line in enumerate(content):
        if re.search(bag, line) and i not in gold_line:
            count += 1
            color = re.search('^[a-z]+ [a-z]+ bag', line).group()
            with_gold.append(color)
            gold_line.append(i)
                
print(count)

bag_dict = {}
def bag_count(bag_type, rules, number=1):
    if bag_type not in bag_dict:   
        for line in rules:
            if re.search(f"^{bag_type}", line):
                inner_bags = re.findall('\d [a-z]+ [a-z]+ bag', line)
                if not inner_bags:
                    inner_bags = 0
                bag_dict[bag_type] = inner_bags
    if bag_dict[bag_type] == 0:
        return 0
    else:
        total = 0
        for _ in range(number):
            for bag in bag_dict[bag_type]:
                count = int(bag[0])
                color = bag[2:]
                total += count + bag_count(color, rules, count)
    return total
            
print(bag_count('shiny gold bag', content))
            