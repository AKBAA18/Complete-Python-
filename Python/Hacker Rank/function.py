# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:27:47 2024

@author: aksha
"""

def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        return leap
    else :
        leap = False
        return leap
year = int(input())
print(is_leap(year))