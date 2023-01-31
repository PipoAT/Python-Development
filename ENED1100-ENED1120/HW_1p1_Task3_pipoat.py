# ENED1120 Week 1 Homework Task 3
# File: HW_1p1_Task3_pipoat
# Date:    18 January 2021
# By:      Andrew Pipo
# Section: 016
# Team:    N/A
# 
# ELECTRONIC SIGNATURE
# Andrew Pipo
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This program will determine the minimum and maximum values
# based on the user input of data points.

choice = "Yes"

datalist = []
while choice == "yes" or choice == "Yes":
    item = input("Enter in values:   ")
    datalist.append(item)
    choice = input("Continue adding values? Enter yes to add more values, and no to determine max/min:   ")  

max_value = None

for num in datalist:
    if (max_value is None or num > max_value):
        max_value = num

minimum = datalist[0]

for number in datalist:
    if minimum > number:
        minimum = number

print("The maximum value is:",max_value)
print("The minimum value is:",minimum)
print("The number of datapoints is:",len(datalist))