BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
nouvelleQuantite_fromage= fromage * nbConvives / BASE
nouvelleQuantite_eau= eau * nbConvives / BASE
nouvelleQuantite_ail= ail * nbConvives / BASE
nouvelleQuantite_pain= pain * nbConvives / BASE

print(nouvelleQuantite_fromage," gr de fromage")
print(nouvelleQuantite_eau," dl d'eau ")
print(nouvelleQuantite_ail," gousse(s) d'ail ")
print(nouvelleQuantite_pain," gr de pain")

