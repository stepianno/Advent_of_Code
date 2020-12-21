#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:09:27 2020

@author: stepianno
"""
from collections import defaultdict

with open('foods.txt') as f:
    content = f.read()
foods = content.split('\n')

allergen_dict = {}
for i, food in enumerate(foods[:-1]):
    allergens = food[:-1].split(' (contains ')[1].split(', ')
    allergen_dict[i] = allergens

allergies = []
for group in allergen_dict.values():
    allergies += group 
allergies = set(allergies)

allergy_dict = defaultdict(list)
for allergy in list(allergies):
    for k,v in allergen_dict.items():
        if allergy in v:
            allergy_dict[allergy].append(k)
            
matches = defaultdict(list)
for k,v in allergy_dict.items():
    words = defaultdict(int)
    for i in v:
        items = foods[i].split(' (contains ')[0].split()
        for item in items:
            words[item] += 1
    for word,count in words.items():
        if count == len(v):
            matches[k].append(word)

match = {}
while len(match) < len(matches):
    for k,v in matches.items():
        if len(v) == 1:
            word = v[0]
            match[k] = word
            for key,val in matches.items():
                if word in val:
                    matches[key].remove(word)
                    
count = 0
for food in foods:
    for word in food.split(' (contains ')[0].split():
        if word not in match.values():
            count += 1
print(count)

canon = []
for ingredient in sorted(match.keys()):
    canon.append(match[ingredient])
print(','.join(canon))