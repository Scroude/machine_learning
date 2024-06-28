import numpy as np

E = np.array([4, 5, 14, 20, 31, 38])

centers = np.array([4, 5, 14])

num_clusters = len(centers)

assignments = np.zeros(len(E), dtype=int)

for iteration in range(1, 100):
    print(f"Itération {iteration}:")

    # Assignation des points aux classes
    for i, obj in enumerate(E):
        distances = np.abs(centers - obj)
        assignments[i] = np.argmin(distances)

    # Mise à jour des centres de gravité
    new_centers = np.array([np.mean(E[assignments == k]) for k in range(num_clusters)])
    print(f"Centres de gravité : {new_centers}")

    # Vérification de la convergence
    if np.all(new_centers == centers):
        break

    centers = new_centers

for k in range(num_clusters):
    print(f"Classe {k+1}: {E[assignments == k]}")
