# Homework Week 11 Assignment 1 Task 1
# File: HW_11p1_Task1_pipoat.py 
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
# This program will determine if the input values are
# within the range of the given model and calculate
# the predicted index for HRI and FRI with presenting
# the respected values and course of action.


# inputs
t = float(input("Enter Outside Temperature (degrees F):   "))
wc = float(input("Enter Weater Condition (cloudy = 0, partly cloudy = 2, sunny = 3):   "))
h = float(input("Enter Relative Humidity:   "))
l = float(input("Enter Number of Ladders on-site:   "))
hstruc = float(input("Enter the height of the structure (ft):   "))
sdry = float(input("Enter Surface Dryness (completely dry = 0, some puddles = 2, completely wet = 3):   "))

# calculations
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
if hstruc < 20 or hstruc > 3800:
    print(hstruc)
    print("value inputed for height of structure is invalid")
if sdry > 3 or sdry == 1 or sdry < 0:
    print(sdry)
    print("value inputed for surface dryness is invalid")

# calculations for all values in range

if (t >= -10 and t <= 125) and (wc == 0 or wc == 2 or wc == 3) and (h >=0 and h <= 1) and (hstruc >= 20 and hstruc <= 2800) and (sdry == 0 or sdry == 2 or sdry == 3):
    HRI = (0.75*t)+(5.0*wc)+(h**2)
    if HRI > 75:
        hcat = 1
        FRI = (0.2*l)+(0.03*hstruc)+(30*hcat)+(10*sdry)
        print("Recommendation: Allow 1 extra break")
        if FRI > 100:
            print("Recommendation: Please hold a quick safety session to remind workers of procedures to avoid fall realted injuries")
    else:
        hcat = 0
        FRI = (0.2*l)+(0.03*hstruc)+(30*hcat)+(10*sdry)
        if FRI > 100:
            print("Recommendation: Please hold a quick safety session to remind workers of procedures to avoud fall realted injuries")
        else:
            print("Safety is Job #1")
else:
    print("See above error messages")