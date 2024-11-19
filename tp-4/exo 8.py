
etudiant1 = {
    'firstname': 'titi',
    'name': 'toto',
    'promo': 2022,
    'group': 202
}

print(f"Votre nom est '{etudiant1['name']}', prénom est '{etudiant1['firstname']}', vous faites partie de la promo {etudiant1['promo']} et votre groupe est {etudiant1['group']}.")


print("\nLes clés du dictionnaire sont :")
for key in etudiant1.keys():
    print(f"- {key}")

print("\nLes valeurs du dictionnaire sont :")
for value in etudiant1.values():
    print(f"- {value}")

print("\nLes tuplets du dictionnaire sont :")
for item in etudiant1.items():
    print(f"- {item}")

etudiant2 = {
    'firstname': 'tutu',
    'name': 'tata',
    'promo': 2023,
    'group': 102
}

binome = {
    'id1': etudiant1,
    'id2': etudiant2
}

print("\nLes étudiants formant le binôme sont :")
for id_etudiant, infos in binome.items():
    print(f"- L'étudiant {infos['name']} {infos['firstname']} du groupe {infos['group']}")
