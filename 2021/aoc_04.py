#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:59:33 2021

@author: stepianno
"""
import numpy as np
with open('bingo.txt') as f:
    content = f.read()
content = content.strip()
boards = content.split('\n\n')
nums = [int(x) for x in boards[0].split(',')]
boards = [[[int(x) for x in line.split()] for line in board.split('\n')] for board in boards[1:]]
boards = np.array(boards)

check = np.zeros(boards.shape)
for n in nums[:4]:
    inds = np.where(boards == n)
    check[inds] = 1
flag = False
end = False
wins = []
for n in nums[4:]:
    if end:
        break
    inds = np.where(boards == n)
    check[inds] = 1
    for b in range(len(check)):
        if end:
            break
        if b in wins:
            continue
        for i in range(5):
            if np.sum(check[b, :, i]) == 5 or np.sum(check[b, i, :]) == 5:
                indices = np.where(check[b,:,:] == 0)
                if not flag:
                    print('part a:', np.sum(boards[b, indices[0], indices[1]])*n)
                flag = True
                wins.append(b)
                if len(wins) == len(boards):
                    print('part b:', np.sum(boards[b, indices[0], indices[1]])*n)
                    end = True
                break