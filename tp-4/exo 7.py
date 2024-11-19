
binome = ('login1', 'login2')
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

nouveau_login = input("Entrez le nouveau login de votre voisin : ")
binome = (binome[0], nouveau_login)
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

try:
    del binome[1]
except TypeError as e:
    print(f"Erreur : {e}")

login3 = input("Entrez le login du troisième étudiant : ")
trinome = binome + (login3,)
print(f"L'étudiant {trinome[0]} est en binôme avec l'étudiant {trinome[1]} et {trinome[2]}")
