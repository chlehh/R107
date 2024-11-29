prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")
prenom2 = input("Entrez votre 2ème prénom : ")
nom2 = input("Entrez votre 2ème nom : ")
nom= nom.upper()
prenom= prenom.capitalize()
nom2=nom2.upper()
prenom2=prenom2.capitalize()
personne=(nom,prenom)
personne2=(nom2,prenom2)
personnes= sorted([personne,personne2])
for personne in personnes:
    print(f"{personne[1]} {personne[0]}")



