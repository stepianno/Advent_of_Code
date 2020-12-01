#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:05:06 2020

@author: stepianno
"""

def prod_2020(nums):
    nums.sort()
    i = 0
    j = -1
    while nums[i] + nums[j] != 2020:
        if nums[i] + nums[j] < 2020:
            i += 1
        else:
            j -= 1
    return nums[i]*nums[j]