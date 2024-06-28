import numpy as np

X = np.array([[0.8, 0.2]])
y = np.array([[0.4]])

W1 = np.array([[0.5, 0.4], [0.3, 0.2]])
W2 = np.array([[0.8], [0.7]])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

learning_rate = 0.1
epochs = 1000

for i in range(epochs):
