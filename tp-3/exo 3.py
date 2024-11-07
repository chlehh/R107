import random
nombre_a_deviner = random.randint(0, 100)
tentatives = 0
print("Devinez le nombre entre 0 et 100.")
while True:
    essai = int(input("Entrez votre tentative : "))
    tentatives += 1
    if essai < nombre_a_deviner:
        print("C'est plus grand!")
    elif essai > nombre_a_deviner:
        print("C'est plus petit!")
    else:
        print(f"Félicitations! Vous avez trouvé le nombre en {tentatives} tentatives.")
        break
