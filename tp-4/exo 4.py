def plus_frequent(L):
    compteur = {}
    for nombre in L:
        compteur[nombre] = compteur.get(nombre, 0) + 1
    plus_frequent_nombre = max(compteur, key=compteur.get)
    frequence_max = compteur[plus_frequent_nombre]
    print(f"Le nombre le plus fréquent dans la liste est : {plus_frequent_nombre} ({frequence_max} fois)")

L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]

plus_frequent(L1)

