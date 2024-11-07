#N = int(input("veuillez entrez la valeur de N :"))
#somme=0
#for i in range(N+1):
    #somme += i
#print("la somme des entiers naturels de 0 a",N,"est",somme)

#while True:
# valeur = int(input("Entrez un nombre (ou 100 pour arrêter) : "))
# if valeur == 100:
#      print("La boucle est terminée.")
#      break
  #  else:
#    print("Vous avez entré : ", valeur)

count_inferieur_10 = 0
count_entre_10_et_15 = 0
count_superieur_ou_egal_15 = 0

for i in range(10):
    while True:
        valeur = float(input(f"Entrez la valeur {i + 1} (comprise entre 0 et 20) : "))

        if 0 <= valeur <= 20:
            break
        else:
            print("La valeur doit être comprise entre 0 et 20. Essayez encore.")


    if valeur < 10:
        count_inferieur_10 += 1
    elif 10 <= valeur < 15:
        count_entre_10_et_15 += 1
    else:
        count_superieur_ou_egal_15 += 1

print("\nRésumé des valeurs:")
print(f"Nombre de valeurs inférieures à 10 : {count_inferieur_10}")
print(f"Nombre de valeurs entre 10 (inclus) et 15 : {count_entre_10_et_15}")
print(f"Nombre de valeurs supérieures ou égales à 15 : {count_superieur_ou_egal_15}")


