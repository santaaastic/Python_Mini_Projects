##Flow:Game of Odd or Even
#Humans to chose between odd or even first --> Computer to chose a random value between 0 and 6 (only integers),
#Humans to #enter a number from 0 and 6(only integers) --> Addition of both values to calculate sum -->
#Check if the sum is even or odd-
#>Compare the result with the choice of humans in step 1 and declare the result

import random as rd
print("Welcome to Santa's odd/even automated game")
def Humans_select():
   Humans_select.Human_selection = input("Select either odd or even. Type o for odd and e for even in lowercase  :  ")
   if Humans_select.Human_selection not in ("o","e"):
       print("Please select a valid entry -- either o or e corresponds to odd or even respectively")
   return Humans_select.Human_selection
Humans_select()

def Computer_select():
    Computer_select.Comp_Selection=rd.randint(0,6)
    return Computer_select.Comp_Selection
Computer_select()

def Human_num():
   Human_num.Human_num_enter=input("Chose a number from 0 to 6 integers only please  : ")
   return Human_num.Human_num_enter
Human_num()

def sum_cal():
    sum1=int(Human_num.Human_num_enter) +int(Computer_select.Comp_Selection)
    if sum1%2==0:
        sum_cal.result="e"
    else:
        sum_cal.result="o"
    return sum_cal.result

sum_cal()

def winner():
    if sum_cal.result==Humans_select.Human_selection:
        
        print("\n Hurray!! You won")
    else:
        
        print("\n Oops... computer won Better Luck next time!")
winner()

