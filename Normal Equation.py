import random as random
import numpy as np
def Normal_Equation(features,labels):
    X_transpose = np.transpose(features)
    X_transpose_X = np.dot(X_transpose, features)
    X_transpose_y = np.dot(X_transpose, labels)
    y_hat = X_transpose_y
    y = labels
    base_price = random.random()
    #price = random.random()
    learning_rate = 0.1
    r = random.random()*0.1  
    b_hat = base_price + learning_rate*(y-y_hat)
    w_hat = []
    for i in range (len(features)-1):
      w_hat.append((features[i] + learning_rate*r*(y-y_hat)))
    sum = 0
    for j in range (len(features)-1):
      sum += (w_hat[i]*features[i])
    W = sum + b_hat
    return W

W = Normal_Equation(features,labels)
print(W)
