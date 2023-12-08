#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:58:16 2023

@author: stepianno
"""
from collections import Counter
import operator
with open("aoc_07_input.txt") as f:
  data = f.read()
data = [x.strip().split() for x in data.strip().splitlines()]

hands = []
tran = str.maketrans('AKQJT', 'TQKJA')
for hand, bid in data:
  rev = hand.translate(tran)
  count = Counter(hand)
  score = 1
  if len(count) == 1:
    score = 7
  elif len(count) == 2:
    if max(count.values()) == 4:
      score = 6
    else:
      score = 5
  elif len(count) == 3:
    if max(count.values()) == 3:
      score = 4
    else:
      score = 3
  elif len(count) == 4:
    score = 2
  ob = {
      'hand': hand,
      'bid': bid,
      'score': score,
      'rev': rev
  }
  hands.append(ob)
hands.sort(key=lambda x: (x['score'], x['rev']), reverse=False)
print('Part 1:', sum([int(x['bid'])*(i+1) for i, x in enumerate(hands)]))

hands = []
tran = str.maketrans('AKQJT', 'TQK0A')
for hand, bid in data:
  rev = hand.translate(tran)
  count = Counter(hand)
  if 'J' in count and len(count) > 1:
    js = count['J']
    del count['J']
    top = max(count.items(), key = operator.itemgetter(1))[0]
    count[top] += js
  score = 1
  if len(count) == 1:
    score = 7
  elif len(count) == 2:
    if max(count.values()) == 4:
      score = 6
    else:
      score = 5
  elif len(count) == 3:
    if max(count.values()) == 3:
      score = 4
    else:
      score = 3
  elif len(count) == 4:
    score = 2
  ob = {
      'hand': hand,
      'bid': bid,
      'score': score,
      'rev': rev
  }
  hands.append(ob)
hands.sort(key=lambda x: (x['score'], x['rev']), reverse=False)
print('Part 2:', sum([int(x['bid'])*(i+1) for i, x in enumerate(hands)]))