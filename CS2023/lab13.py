# CS2023 Lab13

_author_ = "Andrew Pipo"
_credits_ = "none, worked independently"
_email_ = "pipoat@mail.uc.edu" # Your email address

# imports

import pandas as pd
from IPython.display import display
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# calls the data

cali = fetch_california_housing()
cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)
cali_df["MedHouseValue"] = pd.Series(cali.target)

# splits the data to train and test

X_train, X_test, y_train, y_test = train_test_split( cali.data, cali.target,
random_state=11)

# sets Linear Regression and prediction and expected values

regressmu = LinearRegression()
regressmu.fit(X=X_train, y=y_train)

predicted = regressmu.predict(X_test)
expected = y_test

# for loop to print each feature with R2 and MSE scores
print(f"Multiple Linear Progression using ALL features\nR2 score : {metrics.r2_score(expected, predicted)}\nMSE score: {metrics.mean_squared_error(expected, predicted)}\n")

for i in range(8):
    x_train, x_test, y_train, y_test = train_test_split(cali_df.iloc[:,i].values.reshape(-1,1), cali.target, random_state=11)
    regress = LinearRegression()
    regress.fit(X=x_train, y=y_train)
    predicted = regress.predict(x_test)
    expected = y_test
    print(f"Feature {i} has R2 score : {metrics.r2_score(expected, predicted)}\n          has MSE score:  {metrics.mean_squared_error(expected, predicted)}")