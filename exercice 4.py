import random

# Fonction pour générer un tableau de 'nbr' valeurs aléatoires entre 'vmin' et 'vmax'
def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):
    return sum(1 for x in table if x < vseuil)


nb = int(input("Combien de valeurs voulez-vous générer ? "))
vmin = int(input("Quelle est la valeur minimale ? "))
vmax = int(input("Quelle est la valeur maximale ? "))


reponse = input("Vous voulez préciser le seuil ? (Oui/Non) ").strip().lower()


if reponse == 'oui' or reponse == 'o':
    seuil = int(input("Quel est le seuil ? "))
else:
    seuil = 30

print(f"Générer {nb} nombres entiers entre {vmin} et {vmax}")
tab = generer(nb, vmin, vmax)
tab.sort()
print("Tableau généré :")
print(tab)
total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")
