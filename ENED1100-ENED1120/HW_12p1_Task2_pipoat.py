# Homework Week 12 Assignment 1 Task 2
# File: HW_12p1_Task1_pipoat.py
# Date:    18 November 2021
# By:      Andrew Pipo
# Section: 024
# Team:    349
# 
# ELECTRONIC SIGNATURE
# Andrew Pipo
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This program can operate the Sevens Out game

# imports
import random

Dice1 = random.randint(1,6)
Dice2 = random.randint(1,6)

# inputs
S = int(input('Enter the winning score value:   '))
P1 = input('Enter the name of Player 1:   ')
P2 = input('Enter the name of Player 2:   ')

# Determine if winning score is valid
while S < 0:
    print('Winning Score must be positive value. Reenter score value.')
    S = int(input('Enter the winning score value:   '))

# Determine who goes first
while Dice1 == Dice2:
    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)

if Dice1 > Dice2:
    print('{0} goes first' .format(P1))
    PT = 1
else:
    print('{0} goes first' .format(P2))
    PT = 2

input('Hit Enter when Ready')

# Scores of players

SP1 = 0
SP2 = 0

while SP1 < S and SP2 < S:
    print('{0} score {1}' .format(SP1,P1))
    print('{0} score {1} \n' .format(SP2,P2))

    Dice1 = 0
    Dice2 = 0

    if PT == 1:
        A = SP1
    else:
        A = SP2

    while Dice1 + Dice2 != 7 and A < S:
        Dice1 = random.randint(1,6)
        Dice2 = random.randint(1,6)

        if Dice1 == Dice2:
            A = A+2*(Dice1 + Dice2)
        elif Dice1 + Dice2 == 7:
            A=A
        else:
            A = A+Dice1+Dice2
        print('rolled a {0} and a {1}' .format(Dice1,Dice2))

    if PT == 1:
        print('It is your turn {0}' .format(P2))
        PT = 2
        SP1 = A
        input('Hit Enter when Ready')
    else:
        print('It is your turn {0}' .format(P1))
        PT = 1
        SP2 = A
        input('Hit Enter when Ready')

if SP1 > S:
    print('{0} is the winner' .format(P1))
else:
    print('{0} is the winner' .format(P2))

print('{0}:{1}' .format(P1,SP1))
print('{0}:{1}' .format(P2,SP2))