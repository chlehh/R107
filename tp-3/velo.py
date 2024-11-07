def calculer_tarif_heure(debut, fin):
    tarif_1 = 1.0
    tarif_2 = 2.0
    total = 0.0
    heures_1 = 0
    heures_2 = 0
    for heure in range(debut, fin):
        if 0 <= heure < 7 or 17 <= heure < 24:
            heures_1 += 1
        else:
            heures_2 += 1
    total = heures_1 * tarif_1 + heures_2 * tarif_2
    if heures_1 > 0:
        print(f"{heures_1} heure(s) au tarif horaire de {tarif_1} euro(s)")
    if heures_2 > 0:
        print(f"{heures_2} heure(s) au tarif horaire de {tarif_2} euro(s)")
    print(f"Le montant total à payer est de {total} euro(s).")
def demander_heures():
    while True:
        try:
            debut = int(input("Donnez l’heure de début de la location (un entier) : "))
            fin = int(input("Donnez l’heure de fin de la location (un entier) : "))
            if debut < 0 or debut > 24 or fin < 0 or fin > 24:
                print("Les heures doivent être comprises entre 0 et 24 !\n")
            elif debut == fin:
                print("Attention ! l’heure de fin est identique à l’heure de début.\n")
            elif debut > fin:
                print("Attention ! le début de la location est après la fin ...\n")
            else:
                calculer_tarif_heure(debut, fin)
                break
        except ValueError:
            print("Veuillez entrer des nombres entiers valides.\n")
demander_heures()
