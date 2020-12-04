#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:57:54 2020

@author: stepianno
"""
import re

with open('passports.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

passports = []
passport = {}
for line in content:
    if not line:
        passports.append(passport)
        passport = {}
        continue
    keys = re.findall('(byr|iyr|eyr|hgt|hcl|ecl|pid|cid)', line)
    for key in keys:
        value = re.search(f"(?<={key}:)[^ ]+", line).group()
        passport[key] = value

def pass_check(passport):
    items = list(passport)
    checks = ['byr', 'iyr','eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for check in checks:
        if check not in items:
            return False
    try:
        birth = int(passport['byr'])
        iyr = int(passport['iyr'])
        eyr = int(passport['eyr'])
        hgt_units = re.search('(cm|in)', passport['hgt']).group()
        hgt = int(re.search('\d+', passport['hgt']).group())
        hcl = re.search('^#[0-9a-f]{6}$', passport['hcl']).group()
        ecl = re.search('(amb|blu|brn|gry|grn|hzl|oth)',passport['ecl']).group()
        pid = re.match('^[0-9]{9}$', passport['pid']).group()
    except:
        return False
    if birth < 1920 or birth > 2002:
        return False
    if iyr < 2010 or iyr > 2020:
        return False
    if eyr <2020 or eyr > 2030:
        return False
    if hgt_units == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    else: 
        if hgt < 59 or hgt > 76:
            return False
    return True

count = 0
for passport in passports:
    count += 1 if pass_check(passport) else 0
    
print(count)