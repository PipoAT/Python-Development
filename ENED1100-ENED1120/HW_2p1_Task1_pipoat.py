# ENED1120 Week 2 Task 1 Homework
# File: HW_2p1_Task1_pipoat.py
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
# This program can read data from the given text file
# and calculate and print the number of days the dastolic
# pressure was normal, at risk, and high, as well as
# the average pressure, standard deviation, maximum and minimum
# pressures.

import math

DaysNormal = 0
DaysAtRisk = 0
DaysHigh = 0
total = 0
maxvalue = None


File_in = open("HW2p1_Task1.txt","r")
Data = File_in.readlines()
File_in.close()

Normal = []
AtRisk = []
High = []

for i in range(len(Data)):
    Data[i] = float(Data[i])
    num = int(Data[i]) #calculates average
    total += num
    if Data[i] < 80: #calculates the number of days in certain thresholds
        DaysNormal = DaysNormal + 1
        Normal.append(Data[i])
    elif Data[i] >= 80 and Data[i] < 90:
        DaysAtRisk = DaysAtRisk + 1
    elif Data[i] >= 90:
        DaysHigh = DaysHigh + 1
    High.append(Data[i])
    

# calculation for min and max

    for num in High:
        if maxvalue is None or num > maxvalue:
            maxvalue = num

    minimum = Normal[0]
    
    for num in Normal:
        if minimum > num:
            minimum = num

        mean = sum(High) / len(High)
        var = sum(pow(x - mean, 2) for x in High) / len(High)
        stdev = math.sqrt(var)

AveragePressure = total/365



print("The number of days the diastolic pressure was NORMAL:   ",DaysNormal,"Days")
print("The number of days the diastolic pressure was AT RISK:   ",DaysAtRisk," Days")
print("The number of days the diastolic pressure was HIGH:   ",DaysHigh," Days")
print("The average diastolic pressure is: {0:.1f}\n" .format(AveragePressure))
print("The standard deviation of diastolic pressure is: {0:.1f} \n" .format(stdev))
print("The maximum diastolic pressure is: {0:.0f}\n" .format(maxvalue))
print("The minimum diastolic pressure is: {0:.0f}\n" .format(minimum))