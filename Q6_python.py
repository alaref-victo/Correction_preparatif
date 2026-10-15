n = 3
tableau = []

for i in range(1, n + 1):
    ligne = []
    for j in range(1, n + 1):
        ligne.append(i * j)
    tableau.append(ligne)

print(tableau)