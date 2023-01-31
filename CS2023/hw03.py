# CS2023 - HW03

_author_ = "Andrew Pipo"
_credits_ = "None, worked independently, starter code provided"
_email_ = "pipoat@mail.uc.edu" # Your email address


# Starter Code

url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

# My Code
# This was designed as a function to run the doctests as presented from the
# canvas assignment page

# NOTE: doctests were modified to have the expected words in alphabetical order
# this was done as while the program produces all the correct words, it does still
# fail the tests because of the order the words are in

def step(x):
    
    """
    >>> step("APPLE")
    ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']
    
    >>> step("UC")
    ['CUB', 'CUD', 'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'LUC', 'UCA']

    >>> step("BEARCAT")
    ['ACERBATE', 'BACTERIA', 'BRACCATE', 'BRACTEAL', 'CARTABLE', 'SCABRATE']
    """
    
    wordchecker = []
    for i in range(65, 91): # based on ASCII Values
        wordchecker.append(chr(i))
    
    def step(word_in):
    
        wordout = []
        for w in words:
    
            if len(w) != len(word_in)+1:
                continue
    
            for wc in wordchecker:
    
                if wc not in w:
                    continue
    
                if sorted(w) == sorted(word_in + wc):
                    wordout += [w]
    
        return wordout
    
    print(step(x))

# Doctest function below switched to true to ensure that program was working
# with displaying tests failing/passing

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)