import numpy as np

X = np.array([[0.8, 0.2]])  # Données d'entrée
y = np.array([[0.4]])       # Sortie souhaitée

# Initialisation des poids (valeurs aléatoires)
W1 = np.array([[0.5, 0.4], [0.3, 0.2]])  # Poids entre l'entrée et la couche cachée
W2 = np.array([[0.8], [0.7]])           # Poids entre la couche cachée et la sortie

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

learning_rate = 0.1
epochs = 1000

for _ in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X, W1)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, W2)
    output_layer_output = sigmoid(output_layer_input)

    # Calcul de l'erreur
    error = y - output_layer_output

    # Backpropagation
    d_output = error * sigmoid_derivative(output_layer_output)
    error_hidden_layer = d_output.dot(W2.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Mise à jour des poids
    W2 += hidden_layer_output.T.dot(d_output) * learning_rate
    W1 += X.T.dot(d_hidden_layer) * learning_rate

# Prédiction finale
final_output = sigmoid(np.dot(sigmoid(np.dot(X, W1)), W2))
print("Sortie prédite :", final_output)
