# All data printed out below for last run of this code
# Actual code presented below this data
# CS2023 - Lab10


_author_ = "Andrew Pipo"
_credits_ = "https://www.youtube.com/watch?v=BXkqEXjBf5s&ab_channel=MachineLearning"
_email_ = "pipoat@mail.uc.edu" # Your email address

# Estimators Amount: 10     20     30     40     50     60     70     80     90
# Accuracy:          78.69  85.25  81.97  86.89  83.61  83.61  81.97  86.89  80.33
0
# Based on the data, using 40 or 80 estimators would be the most accurate

# Actual printed data below:

"""
0.9958677685950413
0.819672131147541

              precision    recall  f1-score   support

           0       0.81      0.83      0.82        30
           1       0.83      0.81      0.82        31

    accuracy                           0.82        61
   macro avg       0.82      0.82      0.82        61
weighted avg       0.82      0.82      0.82        61

[[25  5]
 [ 6 25]]

trying model with 10 estimators
model accuracy on test set: 78.69%
trying model with 20 estimators
model accuracy on test set: 85.25%
trying model with 30 estimators
model accuracy on test set: 81.97%
trying model with 40 estimators
model accuracy on test set: 86.89%
trying model with 50 estimators
model accuracy on test set: 83.61%
trying model with 60 estimators
model accuracy on test set: 83.61%
trying model with 70 estimators
model accuracy on test set: 81.97%
trying model with 80 estimators
model accuracy on test set: 86.89%
trying model with 90 estimators
model accuracy on test set: 80.33%
"""


# Starter Code
import pandas as pd 
import numpy as np 

heart_disease = pd.read_csv('C:\Programming\Python\heart.csv') 
X = heart_disease.drop(['target'] , axis=1)  # features matrix
Y = heart_disease['target'] # labels matrix

# Choosing right model and hyperparameters explained via video
from sklearn.ensemble import RandomForestClassifier  
clf = RandomForestClassifier(n_estimators=10) 

# Fit model to data
from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2) 
clf.fit(X_train, Y_train) 
y_pred = clf.predict(X_test) 

# Evalulate the model on the training data and test dataa per video
print(clf.score(X_train, Y_train)) 
print(clf.score(X_test, Y_test))

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(classification_report(Y_test, y_pred))
print(confusion_matrix(Y_test, y_pred))
print(accuracy_score(Y_test, y_pred))

# Improving a model
# Trying diffrerent amount of n_estimators per video
np.random.seed(42)
for i in range(10, 100, 10):
    print(f"trying model with {i} estimators")
    clif = RandomForestClassifier(n_estimators=i).fit(X_train, Y_train)
    print(f"model accuracy on test set: {clif.score(X_test, Y_test) * 100:.2f}%")
    
# Save model and loading per video
import pickle
pickle.dump(clf, open("random_forst_model_2.pkl","wb"))
    
    

 