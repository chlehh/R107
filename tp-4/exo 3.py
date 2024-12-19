def calcul_produit_scalaire():
    nMax = 3
    while True:
        n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
        if 1 <= n <= nMax:
            break
        else:
            print(f"Veuillez entrer un nombre entre 1 et {nMax}.")
    v1 = []
    v2 = []
    print("Saisie du premier vecteur :")
    for i in range(n):
        v1.append(int(input(f"v1[{i}] = ")))
    print("Saisie du second vecteur :")
    for i in range(n):
        v2.append(int(input(f"v2[{i}] = ")))
    produit_scalaire = sum(v1[i] * v2[i] for i in range(n))
    print(f"\nLe produit scalaire de v1 par v2 vaut {produit_scalaire}.")
calcul_produit_scalaire()
-------------------------
def produit_scalaire():
    # Taille maximale des vecteurs
    nMax = 3
    
    # Demander à l'utilisateur la taille des vecteurs
    while True:
        n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
        if 1 <= n <= nMax:
            break
        else:
            print(f"Veuillez entrer une taille entre 1 et {nMax}.")
    
    # Déclarer les vecteurs v1 et v2
    v1 = []
    v2 = []
    
    # Saisie du premier vecteur
    print("Saisie du premier vecteur :")
    for i in range(n):
        v1.append(int(input(f"v1[{i}] = ")))
    
    # Saisie du second vecteur
    print("Saisie du second vecteur :")
    for i in range(n):
        v2.append(int(input(f"v2[{i}] = ")))
    
    # Calcul du produit scalaire
    produit = sum(v1[i] * v2[i] for i in range(n))
    
    # Affichage du résultat
    print(f"Le produit scalaire de v1 par v2 vaut {produit}.")
    
# Appel de la fonction
produit_scalaire()

