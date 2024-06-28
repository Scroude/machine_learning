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
        
    