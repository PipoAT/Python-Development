# Homework Week 12 Assignment 1 Task 1
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
# This program can calculate the impact time and the max height
# based on the input of the angle of increment and initial velocity.

# imports
import math

# defined variables

g = 9.81 # m/s/s
k = 0

# input

vo = float(input("Input initial velocity:   "))
ai = float(input("Input angle increment:   "))
ai = math.radians(ai)

while vo < 0 or (ai < 0 or ai > 90):
    print("Values are invalid. Initial Velocity must be postivie and angle increment must be between 0 and 90")
    vo = float(input("Input initial velocity:   "))
    ai = float(input("Input angle increment:   "))

# calculations

if vo > 0 and (ai >= 0 and ai <= 90):
    for i in range(4):
        k = k+1
        af = k*ai
        impacttime = ((2*vo*math.sin(af))/g)
        maxheight = (vo**2)*((math.sin(af)**2)/(2*g))
        if math.degrees(af) <= 90:
            print('Angle of Increment is: {0:.2f} Degrees \n' .format(math.degrees(af)), 'The impact time is: {0:.2f} Seconds \n' .format(impacttime), 'The max height is: {0:.2f} Meters \n' .format(maxheight))
    
