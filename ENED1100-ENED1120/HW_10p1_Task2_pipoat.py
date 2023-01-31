# Homework Week 10 Assignment 1 Task 2
# File: HW_10p1_Task2_pipoat.py 
# Date:    31 October 2021
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
# This program will calculate the incident, reflected, and transmitted angle
# as well as the reflected and transmitted amplitudes.


# imports

import math

# inputs

n1 = float(input("Input the intrinsic impedance of material 1:   "))
b1 = float(input("Input the phase constant of material 1:   "))
n2 = float(input("Input the intrinsic impedance of material 2:   "))
b2 = float(input("Input the phase constant of material 2:   "))
a = float(input("Input the amplitude of the incident wave:   "))

# calculations
# thetaR is theta I

thetaAB = math.asin(math.sqrt(((b2**2)*((n2**2)-(n1**2)))/(((n2**2)*(b1**2))-((n1**2)*(b2**2)))))

thetaT = math.acos((n1*(math.cos(thetaAB)))/(n2))

et = ((2*n2*math.cos(thetaAB))/((n2*math.cos(thetaT))+(n1*math.cos(thetaAB))))*a

er = (((n2*math.cos(thetaAB))-(n1*math.cos(thetaT)))/((n2*math.cos(thetaAB))+(n1*math.cos(thetaT))))*a

thetaAB = math.degrees(thetaAB)

thetaT = math.degrees(thetaT)


# results
# the incident and reflected angles are the same, thus thetaAB is printed twice

print("The Incident Angle is: {0:.2f} Degrees \n".format(thetaAB))
print("The Reflected Angle is: {0:.2f} Degrees \n".format(thetaAB))
print("The Transmitted Angle is: {0:.2f} Degrees \n".format(thetaT))
print("The Reflected Amplitude is: {0:.2f} V/m \n".format(er))
print("The Transmitted Amplitude is: {0:.2f} V/m \n".format(et))




