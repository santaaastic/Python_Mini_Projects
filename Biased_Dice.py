# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 07:42:23 2021

Biased Dice:
    
    Build a automatic biased dice which shows six more often than other numbers

@author: Shantanu
"""

import random as rd

def rand():
    rand.generate=rd.randint(1,12)
    return rand.generate
rand()

def bias():
    if rand.generate>=6:
        bias.result=6
    else:
        bias.result=rand.generate
    print("Dice is being rolled... ")
    print(bias.result)
    return bias.result
bias()