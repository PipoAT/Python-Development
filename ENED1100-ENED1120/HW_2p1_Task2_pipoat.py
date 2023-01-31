# ENED1120 Week 2 Task 2 Homework
# File: HW_2p1_Task2_pipoat.py
# Date:    27 January 2021
# By:      Andrew Pipo
# Section: 016
# Team:    234
# 
# ELECTRONIC SIGNATURE
# Andrew Pipo
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This program can read the provided file, and calculate the
# refracted angles for each row of values in the file and write
# it into a new text file

import math
from re import I

File_in = open("Refraction.txt","r")
Data = File_in.readlines()
File_in.close()

N1 = []
THETA1 = []
THETA2 = []
RADIANS = []
RADIANS2 = []
N2 = []
HEADERS = ["n1","Theta1","n2","Theta2"]



for i in range(1,len(Data)):
    Line = Data[i].split()
    n1 = float(Line[0])
    theta = float(Line[1])
    n2 = float(Line[2])
    N1.append(n1)
    THETA1.append(theta)
    N2.append(n2)

for i in range(len(THETA1)):
    rad = THETA1[i]*(math.pi/180)
    RADIANS.append(rad)
    rad2 = N1[i]*math.sin(RADIANS[i]) / N2[i]
    rad2 = math.asin(rad2)
    finalT2 = rad2*(180/math.pi)
    finalT2 = round(finalT2,1)
    THETA2.append(finalT2)
    

New_file = open("HW_2p1_Task2.txt",'w')
New_file.write(HEADERS[0])
New_file.write("    ")
New_file.write(HEADERS[1])
New_file.write("    ")
New_file.write(HEADERS[2])
New_file.write("    ")
New_file.write(HEADERS[3])

for i in range(len(THETA2)):
    New_file.write("\n")
    New_file.write("{0:.3f}".format((N1[i])))
    New_file.write("   ")
    New_file.write("{0:.1f}".format(THETA1[i]))
    New_file.write("    ")
    New_file.write("{0:.3f}".format(N2[i]))
    New_file.write("    ")
    New_file.write("{0:.1f}".format(THETA2[i]))

New_file.close()


