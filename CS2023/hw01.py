
# CS2023 Python Programming Challenge #1

_author_ = "Andrew Pipo"
_credits_ = "Refered to GCD code linked below for developing the code for the calculations"
_email_ = "pipoat@mail.uc.edu" # Your email address


# defined function egypt

def egypt(p,q):
    
    """
    >>> egypt(3,4)
    '1/2 + 1/4 = 3/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12 = 11/12'
    
    
## BELOW COMMENTS WERE PROVIDED FROM CANVAS ON THE ASSIGNMENT
## Partial credit will be given for code that passes the two given doctests. 
## For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
## These are more difficult and may require you to develop faster, more efficient code.
## Hint: you may consider using code for gcd function for greatest common divisor:
## https://www.geeksforgeeks.org/gcd-in-python/

    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112 = 123/124'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424 = 103/104'
    
    # doctests 3 and 4 modifed from provided canvas doctest to match formatting with
    # doctests 1 and 2, adding "= p/q" fraction at the end of each doctest statement 
    
    >>> egypt(45,46)
    '1/2 + 1/3 + 1/7 + 1/483 = 45/46'
    >>> egypt(200,201)
    '1/2 + 1/3 + 1/7 + 1/54 + 1/3166 + 1/40091058 = 200/201'
    """
    # added doctests 5 and 6 to ensure code covered a larger span of values for
    # p and q
    
    numer = p
    denom = q

    # list for denom
    dList = []

    # calculations for each fraction and stores them
    # in a list. Designed to accomidate for large fractions
    # to avoid overflow errors
    while numer != 0:

        if denom % numer == 0:
            unit = denom // numer
        else:
            unit = (denom // numer) + 1

        dList.append(unit)

        numer = (numer*unit) - denom
        denom = denom*unit


    # print statement to display the first ' for formatting
    print('\'', sep='', end='')

    # for loop to execute printing off the fractions
    for i in range(len(dList)):
        print(f"1/{dList[i]}",end="")
        if i >= len(dList)-1:
                print(f" = {p}/{q}",end="'")
                break
        else:
            print(" + ",end="")
       

## Partial credit will be given for code that passes the two given doctests. 
## For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
## These are more difficult and may require you to develop faster, more efficient code.

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)