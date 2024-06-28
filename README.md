## K-Moy
### Décomposition du code

1.  **Importation de la bibliothèque NumPy** :
    
    `import numpy as np` 
    
    Le code utilise NumPy, une bibliothèque populaire pour les calculs numériques en Python, ce qui permet de gérer efficacement des tableaux multidimensionnels et de réaliser des opérations vectorisées.
    
2.  **Définition de l'ensemble de données** :
    
    `E = np.array([4, 5, 14, 20, 31, 38])` 
    
    `E` est un tableau NumPy contenant les points de données à regrouper en clusters. Dans ce cas, il s'agit de six valeurs numériques.
    
3.  **Initialisation des centres des clusters** :

    `centers = np.array([4, 5, 14])` 
    
    `centers` est un tableau NumPy qui contient les positions initiales des centres des clusters. Le nombre de clusters est déterminé par le nombre de valeurs dans ce tableau, ici trois centres initialisés à 4, 5 et 14.
    
4.  **Nombre de clusters** :
    
    `num_clusters = len(centers)` 
    
    `num_clusters` contient le nombre de clusters, calculé comme la longueur du tableau `centers`. Ici, il est égal à 3.
    
5.  **Tableau des affectations** :
    
    `assignments = np.zeros(len(E), dtype=int)` 
    
    `assignments` est un tableau de zéros de la même longueur que `E`, qui stockera les indices des clusters assignés pour chaque point de données. Chaque entrée de `assignments` indique à quel cluster le point correspondant de `E` est assigné.
    
6.  **Boucle de l'algorithme des k-moyennes** :
    
    `for iteration in range(1, 100):` 
    
    Une boucle qui exécute l'algorithme pour un maximum de 99 itérations (de 1 à 99 inclus). L'objectif est de trouver la configuration stable des clusters avant d'atteindre ce nombre maximal d'itérations.
    
    -   **Affichage de l'itération courante** :
        
        `print(f"Itération {iteration}:")` 
        
    -   **Calcul des distances et affectation des points** :

        `for i, obj in enumerate(E):
            distances = np.abs(centers - obj)
            assignments[i] = np.argmin(distances)` 
        
        Pour chaque point de `E`, le code calcule les distances absolues entre ce point et chacun des centres de clusters (`centers`). Le point est ensuite assigné au cluster dont le centre est le plus proche (`np.argmin(distances)`).
        
    -   **Calcul des nouveaux centres des clusters** :
        
        `new_centers = np.array([np.mean(E[assignments == k]) for k in range(num_clusters)])
        print(f"Centres de gravité : {new_centers}")` 
        
        Les nouveaux centres des clusters sont calculés comme la moyenne des points actuellement assignés à chaque cluster (`assignments == k`). Cette moyenne est calculée pour chaque cluster `k`, et les résultats sont stockés dans `new_centers`.
        
    -   **Condition d'arrêt** :
        
        `if np.all(new_centers == centers):
            break` 
        
        Si les nouveaux centres calculés (`new_centers`) sont identiques aux centres précédents (`centers`), l'algorithme est considéré comme convergé, et la boucle est interrompue.
        
    -   **Mise à jour des centres** :
        
        `centers = new_centers` 
        
        Les centres des clusters sont mis à jour pour être utilisés dans l'itération suivante.
        
7.  **Affichage des résultats** :
    
    `for k in range(num_clusters):
        print(f"Classe {k+1}: {E[assignments == k]}")` 
    
    Après la convergence de l'algorithme ou la fin des itérations, le code affiche les points de chaque cluster. Chaque cluster `k` est affiché avec ses points assignés.
    

### Comportement du Code

1.  **Initialisation** : Les points de données sont initialement assignés aux clusters basés sur les centres de clusters donnés.
2.  **Itération** : À chaque itération, l'algorithme :
    -   Assigne chaque point de données au cluster le plus proche.
    -   Recalcule les centres des clusters comme la moyenne des points assignés à chaque cluster.
    -   Vérifie si les centres des clusters ont changé par rapport à l'itération précédente.
3.  **Convergence** : Le processus se répète jusqu'à ce que les centres des clusters ne changent plus ou que le nombre maximal d'itérations soit atteint.
4.  **Résultat final** : Les points de données sont affichés regroupés par cluster.
## Perceptron
### Décomposition du code

1.  **Initialisation des poids** :

    `w_0 = 0.05 w_1 = 0.1 w_2 = 0.2`

    
	Les poids initiaux w0w_0w0​, w1w_1w1​, et w2w_2w2​ sont définis. Ces poids sont utilisés pour combiner linéairement les entrées.
    
2.  **Coefficient d'apprentissage** 
    
    `coef_app = 0.1` 
    
    Le coefficient d'apprentissage α\alphaα est fixé à 0.1. Ce paramètre contrôle l'ampleur des ajustements des poids à chaque itération.
    
3.  **Ensemble de données d'entrée-sortie** :
    
    `entree_sortie = [
        [1, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]
    ]` 
    
    C'est une liste de listes où chaque sous-liste représente une combinaison d'entrées et une sortie attendue. Par exemple, `[1, 0, 0, 0]` signifie que les entrées sont 1, 0, 0 et la sortie attendue est 0.
    
4.  **Boucle principale de mise à jour des poids** :
    
    `for i in entree_sortie:
        for j in entree_sortie:
            print(f"Entree = {j[0]}, {j[1]}, {j[2]} Sortie attendue = {j[3]}")
            w_i_x_i = round(w_0 * j[0] + w_1 * j[1] + w_2 * j[2], 2)
            print(f"WiXi = {w_i_x_i}")
            ...
        break` 
    
    Ce code comporte une double boucle imbriquée sur `entree_sortie`, mais la boucle externe est interrompue immédiatement après sa première itération à cause de `break`. Par conséquent, chaque combinaison d'entrée-sortie n'est effectivement traitée qu'une seule fois.
    
5.  **Calcul de la somme pondérée** :

    `w_i_x_i = round(w_0 * j[0] + w_1 * j[1] + w_2 * j[2], 2)` 
    
    Pour chaque ensemble d'entrées `j[0]`, `j[1]`, `j[2]`, la somme pondérée est calculée en utilisant les poids initiaux. Cette somme w_i_x_i représente une combinaison linéaire des entrées pondérées par les poids.
    
6.  **Mise à jour des poids** : Les poids sont ajustés si la somme pondérée ne correspond pas à la sortie attendue :
    
    -   **Si la somme pondérée est positive mais la sortie attendue est 0** :
        
        `if w_i_x_i > 0 and j[3] == 0:
            print("Sortie différente de celle attendue, Calcul des nouveaux poids")
            dw_0 = coef_app * (j[3] - 1) * j[0]
            dw_1 = coef_app * (j[3] - 1) * j[1]
            dw_2 = coef_app * (j[3] - 1) * j[2]
            w_0 = w_0 + dw_0
            w_1 = w_1 + dw_1
            w_2 = w_2 + dw_2
            print(f"W0 = {w_0} W1 = {w_1} W2 = {w_2}")` 
        
        Dans ce cas, les poids sont ajustés pour diminuer leur contribution, car la sortie attendue est inférieure à la sortie prédite.
        
    -   **Si la somme pondérée est négative mais la sortie attendue est 1** :
        
        `if w_i_x_i < 0 and j[3] == 1:
            print("Sortie différente de celle attendue, Calcul des nouveaux poids")
            dw_0 = coef_app * (j[3] - 0) * j[0]
            dw_1 = coef_app * (j[3] - 0) * j[1]
            dw_2 = coef_app * (j[3] - 0) * j[2]
            w_0 = w_0 + dw_0
            w_1 = w_1 + dw_1
            w_2 = w_2 + dw_2
            print(f"W0 = {w_0} W1 = {w_1} W2 = {w_2}")` 
        
        Ici, les poids sont ajustés pour augmenter leur contribution, car la sortie attendue est supérieure à la sortie prédite.
        

### Comportement du Code

-   **Initialisation** : Les poids sont initialement définis à de petites valeurs positives.
-   **Boucle de mise à jour** : Pour chaque combinaison d'entrée-sortie, le code imprime les valeurs actuelles des entrées et la sortie attendue, calcule la somme pondérée et ajuste les poids si nécessaire.
-   **Condition de correction** : Les poids sont modifiés seulement si la prédiction est incorrecte par rapport à la sortie attendue.
-   **Apprentissage** : La mise à jour des poids suit la règle de correction, qui est une forme simplifiée de l'apprentissage supervisé.
## XOR
### Décomposition du code

1.  **Importation de NumPy** :
    
    `import numpy as np` 
    
    La bibliothèque NumPy est importée pour faciliter les opérations sur les tableaux, qui sont essentiels pour les calculs de réseaux de neurones.
    
2.  **Définition des entrées et de la sortie** :
    
    `X = np.array([[0.8, 0.2]])  # Entrées
    y = np.array([[0.4]])       # Sortie attendue` 
    
    -   `X` est une matrice d'entrée contenant un seul exemple avec deux caractéristiques : X=[[0.8,0.2]]X = [[0.8, 0.2]]X=[[0.8,0.2]].
    -   `y` est la sortie attendue pour cet exemple : y=[[0.4]]y = [[0.4]]y=[[0.4]].
3.  **Initialisation des poids** :
    
    `W1 = np.array([[0.5, 0.4], [0.3, 0.2]])  # Poids de la couche cachée
    W2 = np.array([[0.8], [0.7]])            # Poids de la couche de sortie` 
    
    -   `W1` est la matrice de poids pour les connexions entre les neurones d'entrée et les neurones de la couche cachée.
    -   `W2` est la matrice de poids pour les connexions entre les neurones de la couche cachée et le neurone de sortie.
4.  **Définition de la fonction sigmoïde et de sa dérivée** :
    
    `def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(x):
        return x * (1 - x)` 
    
    -   `sigmoid(x)` est la fonction d'activation sigmoïde, qui transforme les valeurs d'entrée en une sortie entre 0 et 1.
    -   `sigmoid_derivative(x)` calcule la dérivée de la fonction sigmoïde, utilisée dans la rétropropagation pour ajuster les poids.
5.  **Définition du taux d'apprentissage et du nombre d'époques** :
    
    `learning_rate = 0.1
    epochs = 1000` 
    
    -   `learning_rate` est le facteur par lequel les mises à jour des poids sont multipliées. Il contrôle la taille des ajustements des poids à chaque itération.
    -   `epochs` est le nombre de fois que le réseau de neurones parcourt l'ensemble des données d'entraînement.
6.  **Boucle d'entraînement du réseau de neurones** :
    
    `for _ in range(epochs):` 
    
    Cette boucle s'exécute pour un nombre fixé d'époques, mettant à jour les poids à chaque itération.
    
    -   **Calcul des activations de la couche cachée** :
        
        `hidden_layer_input = np.dot(X, W1)
        hidden_layer_output = sigmoid(hidden_layer_input)` 
        
        Les entrées `X` sont multipliées par les poids `W1` pour obtenir les activations de la couche cachée (`hidden_layer_input`), puis transformées par la fonction sigmoïde pour obtenir les sorties de la couche cachée (`hidden_layer_output`).
        
    -   **Calcul de la sortie du réseau** :
        
        `output_layer_input = np.dot(hidden_layer_output, W2)
        output_layer_output = sigmoid(output_layer_input)` 
        
        Les sorties de la couche cachée sont multipliées par les poids `W2` pour obtenir les activations de la couche de sortie (`output_layer_input`), qui sont ensuite transformées par la fonction sigmoïde pour obtenir la sortie finale du réseau (`output_layer_output`).
        
    -   **Calcul de l'erreur de sortie** :
        
        `error = y - output_layer_output` 
        
        L'erreur est la différence entre la sortie attendue `y` et la sortie prédite `output_layer_output`.
        
    -   **Calcul du gradient de la couche de sortie** :
        
        `d_output = error * sigmoid_derivative(output_layer_output)` 
        
        Le gradient pour la couche de sortie (`d_output`) est calculé en multipliant l'erreur par la dérivée de la fonction sigmoïde de la sortie de la couche de sortie.
        
    -   **Propagation de l'erreur vers la couche cachée** :
        
        `error_hidden_layer = d_output.dot(W2.T)
        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)` 
        
        L'erreur est propagée vers la couche cachée (`error_hidden_layer`), et le gradient pour la couche cachée (`d_hidden_layer`) est calculé de manière similaire.
        
    -   **Mise à jour des poids** :
        
        `W2 += hidden_layer_output.T.dot(d_output) * learning_rate
        W1 += X.T.dot(d_hidden_layer) * learning_rate` 
        
        Les poids `W2` et `W1` sont mis à jour en utilisant les gradients calculés, multipliés par le taux d'apprentissage.
        
7.  **Calcul de la sortie finale après l'entraînement** :
    
    `final_output = sigmoid(np.dot(sigmoid(np.dot(X, W1)), W2))
    print("Sortie prédite :", final_output)` 
    
    Après l'entraînement, le réseau de neurones est testé sur la même entrée pour voir la sortie prédite finale.
