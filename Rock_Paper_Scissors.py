# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:00:35 2021

@author: Shantanu Srivastava

Game of Rock Papers & Scissors

"""

import random as rd
def rand1():
    rand1.comp_select=rd.randint(1, 3)
rand1()
def comp():
    if rand1.comp_select==1:
        comp.comp_select1="r"
    elif rand1.comp_select==2:
        comp.comp_select1="p"
    else:
        comp.comp_select1="s"
    return comp.comp_select1
comp()

def user():
    print("Welcome to the game of Rock paper scissors!")
    user.user_select=input("Enter r for rock, p for paper and s for scissors  :  ")
    return user.user_select
user()

def rps():
    if comp.comp_select1==user.user_select:
        rps.result=print("\n The match is tied as both you and computer selected the same entity")
    elif comp.comp_select1=="r" and user.user_select=="p":
        rps.result=print("\n Computer selected rock and you selected paper, You win!!")
    elif comp.comp_select1=="r" and user.user_select=="s":
        rps.result=print("\n Computer selected rock and you selected scissor, Computer wins!!")
    elif comp.comp_select1=="p" and user.user_select=="r":
        rps.result=print("\n Computer selected paper and you selected rock, Computer wins!!")
    elif comp.comp_select1=="p" and user.user_select=="s":
        rps.result=print("\n Computer selected paper and you selected scissor, You win!!")   
    elif comp.comp_select1=="s" and user.user_select=="r":
        rps.result=print("\n Computer selected scissor and you selected rock, You win!!")
    elif comp.comp_select1=="s" and user.user_select=="p":
        rps.result=print("\n Computer selected scissor and you selected paper, Computer wins!!" ) 
    return rps.result
rps()   
        