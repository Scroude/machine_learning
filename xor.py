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

for _ in range(epochs):
    hidden_layer_input = np.dot(X, W1)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, W2)
    output_layer_output = sigmoid(output_layer_input)

    error = y - output_layer_output

    d_output = error * sigmoid_derivative(output_layer_output)
    error_hidden_layer = d_output.dot(W2.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    W2 += hidden_layer_output.T.dot(d_output) * learning_rate
    W1 += X.T.dot(d_hidden_layer) * learning_rate

final_output = sigmoid(np.dot(sigmoid(np.dot(X, W1)), W2))
print("Sortie prédite :", final_output)
