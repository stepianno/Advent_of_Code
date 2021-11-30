#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:24:01 2020

@author: stepianno
"""
def add_prod(nums, target):
    i = 0
    j = -1
    while nums[i] + nums[j] != target:
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return (nums[i],nums[j])

def tri_prod_2020(nums):
    nums.sort()
    for i, n in enumerate(nums):
        target = 2020 - n
        try:
            x,y = add_prod(nums[i+1:], target)
            return n*x*y
        except:
            continue