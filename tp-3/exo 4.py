
n = int(input("Entrez un entier positif n pour calculer sa factorielle : "))
if n < 0:
    print("La factorielle n'est définie que pour les entiers positifs.")
else:
    choix_boucle = input("Choisissez le type de boucle (for/while) : ").strip().lower()
    if choix_boucle == "for":
        factorielle = 1
        for i in range(1, n + 1):
            factorielle *= i
            print(f"Étape {i}: {factorielle}")
    elif choix_boucle == "while":
        factorielle = 1
        i = 1
        while i <= n:
            factorielle *= i
            print(f"Étape {i}: {factorielle}")
            i += 1
    else:
        print("Choix de boucle invalide. Veuillez entrer 'for' ou 'while'.")
    print(f"La factorielle de {n} est : {factorielle}")
