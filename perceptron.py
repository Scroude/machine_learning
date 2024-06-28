w_0 = 0.05
w_1 = 0.1
w_2 = 0.2

coef_app = 0.1

entree_sortie = [[1, 0, 0, 0],
                 [1, 0, 1, 1],
                 [1, 1, 0, 1],
                 [1, 1, 1, 1]]


def apprentissage():
    global w_0, w_1, w_2
    for i in entree_sortie:
        for j in entree_sortie:
            print(f"Entree = {j[0]}, {j[1]}, {j[2]} Sortie attendue = {j[3]}")
            w_i_x_i = round(w_0 * j[0] + w_1 * j[1] + w_2 * j[2], 2)
            print(f"WiXi = {w_i_x_i}")
            if w_i_x_i > 0 and j[3] == 0:
                print("Sortie différente de celle attendue, Calcul des nouveaux poids")
                dw_0 = coef_app * (j[3] - 1) * j[0]
                dw_1 = coef_app * (j[3] - 1) * j[1]
                dw_2 = coef_app * (j[3] - 1) * j[2]
                w_0 = w_0 + dw_0
                w_1 = w_1 + dw_1
                w_2 = w_2 + dw_2
                print(f"W0 = {w_0} W1 = {w_1} W2 = {w_2}")
            elif w_i_x_i <= 0 and j[3] == 1:
                print("Sortie différente de celle attendue, Calcul des nouveaux poids")
                dw_0 = coef_app * (j[3] - 0) * j[0]
                dw_1 = coef_app * (j[3] - 0) * j[1]
                dw_2 = coef_app * (j[3] - 0) * j[2]
                w_0 = w_0 + dw_0
                w_1 = w_1 + dw_1
                w_2 = w_2 + dw_2
                print(f"W0 = {w_0} W1 = {w_1} W2 = {w_2}")
            print(f"W0 = {w_0} W1 = {w_1} W2 = {w_2}")
        break





def evaluation():
    entree = [1, 0.4, 0.8]
    print(entree)
    w_i_x_i = round(w_0 * entree[0] + w_1 * entree[1] + w_2 * entree[2], 2)
    print(f"Sortie = {w_i_x_i}")


print("Phase apprentissage")
apprentissage()
print("Phase d'évaluation")
evaluation()
