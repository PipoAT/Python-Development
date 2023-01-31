# CS2023 Lab14

_author_ = "Andrew Pipo"
_credits_ = "none, worked independently"
_email_ = "pipoat@mail.uc.edu" # Your email address

# imports
import numpy as np
from random import random
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


totalball = np.arange(1,1000,1)
bin_empty = []
numBins = 0

for N in totalball:
    numBins = 0
    bins = np.zeros(N)
    
    for b in range(N):
        bins[int(N*random())] += 1
        
    for i in bins:
        if i == 0:
            numBins += 1
            
    bin_empty.append(numBins)
    
# plotting the graph
plt.plot(totalball, bin_empty)
plt.show()

x = totalball.reshape(-1,1)
y = bin_empty

model = LinearRegression().fit(x,y)
intercept = model.intercept_
rvalue = model.score(x,y)
slope = model.coef_

print("SciPy Linear Regression Solution")
print(' slope: ', (float(slope)))
print(' intercept ', (float(intercept)))
print(' rvalue: ', (rvalue))
