# Homework Week 11 Assignment 1 Task 2
# File: HW_11p1_Task2_pipoat.py 
# Date:    11 November 2021
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
# This program will determine if construction workers need extra
# breaks using another algorithm similar to the used in Task 1.

# inputs
t = float(input("Enter Outside Temperature (degrees F):   "))
wc = float(input("Enter Weater Condition (rainy = 0, cloudy = 2, sunny = 3):   "))
h = float(input("Enter Relative Humidity:   "))

# Are values in range?
# Provides error message if outside of range

if t < -10 or t > 125:
    print(t)
    print("value inputed for temperature is invalid")
if wc > 3 or wc == 1 or wc < 0:
    print(wc)
    print("value inputed for weather condition is invalid")
if h < 0 or h > 1:
    print(h)
    print("value inputed for relative humidity is invalid")
    

# calculation for if all values are in range

if (t >= -10 and t <=125) and (wc == 0 or wc == 2 or wc == 3) and (h >= 0 and h <= 1):
    if wc == 0:
        print("Recommendation: Work Inside")
    else:
        if t >= 90:
            if h > .8 and wc == 3:
                print("Recommdendation: Give two 15 minute breaks")
            elif h > .9 and wc ==2:
                print("Recommendation: Give one 15 minute break")
            else:
                print("Recommendation: Give one 10 minute break")
        elif t > 80 and t < 90 and wc == 3 and h > .9:
            print("Recommendation: Give two 10 minute breaks")
        elif t > 80 and t < 90 and (h > .9 or wc ==3):
            print("Recommendation: Give one 10 minute break")
        else:
            print("Recommendation: No extra breaks")
else:
    print("See error messages above")