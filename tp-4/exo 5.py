def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)
def verifier_date(date):
    if len(date) != 8 or not date.isdigit():
        print("Format incorrect. Veuillez entrer une date sous le format jjmmaaaa.")
        return
    jour = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])
    if mois < 1 or mois > 12:
        print("Mois invalide. Le mois doit être entre 01 et 12.")
        return
    jours_par_mois = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if est_bissextile(annee):
        jours_par_mois[2] = 29
    if jour < 1 or jour > jours_par_mois.get(mois, 31):
        print(f"Jour invalide. Le mois {mois} n'a pas {jour} jours.")
        return
    print(f"La date {date} est correcte.")
date = input("Entrez une date sous le format jjmmaaaa : ")
verifier_date(date)
