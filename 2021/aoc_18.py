#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 11:36:21 2021

@author: stepianno
"""
from itertools import permutations
with open('snail.txt') as f:
    content = [line.strip() for line in f.readlines()]
snails = [eval(line) for line in content]

def func_add(d1,d2,d3,d4,d5,add):
    if type(arr[d1]) == int:
        arr[d1] += add
    elif type(arr[d1][d2]) == int:
        arr[d1][d2] += add
    elif type(arr[d1][d2][d3]) == int:
        arr[d1][d2][d3] += add
    elif type(arr[d1][d2][d3][d4]) == int:
        arr[d1][d2][d3][d4] += add
    elif type(arr[d1][d2][d3][d4][d5]) == int:
        arr[d1][d2][d3][d4][d5] += add
        
def snail_it(arr):
    done = False
    while not done:
        done = True
        flag = False
        for i, arr_1 in enumerate(arr):
            if flag:
                break
            if type(arr_1) == int:
                continue
            len_1 = len(arr_1)-1
            for j, arr_2 in enumerate(arr_1):
                if flag:
                    break
                if type(arr_2) == int:
                    continue
                len_2 = len(arr_2)-1
                for k, arr_3 in enumerate(arr_2):
                    if flag:
                        break
                    if type(arr_3) == int:
                        continue
                    len_3 = len(arr_3)-1
                    for l, arr_4 in enumerate(arr_3):
                        if type(arr_4) == int:
                            continue
                        left = arr[i][j][k][l][0]
                        right = arr[i][j][k][l][1]
                        if l > 0:
                            func_add(i,j,k,l-1,-1,left)
                        elif k > 0:
                            func_add(i,j,k-1,-1,-1,left)
                        elif j > 0:
                            func_add(i,j-1,-1,-1,-1,left)
                        elif i > 0:
                            func_add(i-1,-1,-1,-1,-1,left)
                        if l < len_3:
                            func_add(i,j,k,l+1,0,right)
                        elif k < len_2:
                            func_add(i,j,k+1,0,0,right)
                        elif j < len_1:
                            func_add(i,j+1,0,0,0,right)
                        elif i < len(arr)-1:
                            func_add(i+1,0,0,0,0,right)
                        
                        arr[i][j][k][l] = 0
                        done = False
                        flag = True
                        break
        for i, arr_1 in enumerate(arr):
            if flag:
                break
            if type(arr_1) == int:
                if arr_1 >= 10:
                    n = []
                    if arr_1 % 2:
                        n = [arr_1 // 2, arr_1 // 2 + 1]
                    else:
                        n = [arr_1 // 2]*2
                    arr[i] = n
                    done = False
                    flag = True
                    break
                continue
            for j, arr_2 in enumerate(arr_1):
                if flag:
                    break
                if type(arr_2) == int:
                    if arr_2 >= 10:
                        n = []
                        if arr_2 % 2:
                            n = [arr_2 // 2, arr_2 // 2 + 1]
                        else:
                            n = [arr_2 // 2]*2
                        arr[i][j] = n
                        done = False
                        flag = True
                        break
                    continue
                for k, arr_3 in enumerate(arr_2):
                    if flag:
                        break
                    if type(arr_3) == int:
                        if arr_3 >= 10:
                            n = []
                            if arr_3 % 2:
                                n = [arr_3 // 2, arr_3 // 2 + 1]
                            else:
                                n = [arr_3 // 2]*2
                            arr[i][j][k] = n
                            done = False
                            flag = True
                            break
                        continue
                    for l, arr_4 in enumerate(arr_3):
                        if type(arr_4) == int:
                            if arr_4 >= 10:
                                n = []
                                if arr_4 % 2:
                                    n = [arr_4 // 2, arr_4 // 2 + 1]
                                else:
                                    n = [arr_4 // 2]*2
                                arr[i][j][k][l] = n
                                flag = True
                                done = False
                                break
    return arr

arr = snails[0]
for snail in snails[1:]:
    arr = [arr, snail]
    arr = snail_it(arr)
def magnitude(arr):
    if type(arr) == int:
        return arr
    return 3*magnitude(arr[0]) + 2*magnitude(arr[1])
print('part a:', magnitude(arr))
snail_combos = permutations(snails, 2)
mags = []
for i in range(len(snails)):
    for j in range(len(snails)):
        if i==j:
            continue
        with open('snail.txt') as f:
            content = [line.strip() for line in f.readlines()]
        snails = [eval(line) for line in content]
        arr = snails[i]
        arr = [arr, snails[j]]
        arr = snail_it(arr)
        mags.append(magnitude(arr))
print('part b:', max(mags))
