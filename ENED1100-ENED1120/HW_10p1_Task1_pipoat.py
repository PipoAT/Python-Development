# Homework Week 10 Assignment 1 Task 1
# File: HW_10p1_Task1_pipoat.py 
# Date:    30 October 2021
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
# This program will calculate the impedances of both materials and the amplitudes
# of the relected and transmitted waves respectively.


#imports

import math

# inputs

er1 = float(input("input relative permittivity of material 1:   "))
ur1 = float(input("input relative permeability of material 1:   "))
er2 = float(input("input relative permittivity of material 2:   "))
ur2 = float(input("input relative permeability of material 2:   "))
er0 = float(input("input amplitude of the incident wave:   "))

# calculations

n1 = 377.14*(ur1/er1)**0.5
n2 = 377.14*(ur2/er2)**0.5
Et0 = ((2*n2)/(n2+n1))*er0
Er0 = ((n2-n1)/(n2+n1))*er0

# results

print("The intrinsic impedance of material 1 is: {0:.2f} Ohms \n" .format(n1))

print("The intrinsic impedance of material 2 is: {0:.2f} Ohms \n" .format(n2))

print("The amplitude of the reflected wave is: {0:.2f} V/m \n" .format(Er0))

print("The amplitude of the transmitted wave is: {0:.2f} V/m \n" .format(Et0))

