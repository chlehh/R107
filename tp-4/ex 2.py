
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
notes = []
somme_notes = 0.0
for i in range(nombreEtudiants):
    while True:
        note = float(input(f"Note etudiant {i} : "))
        if 0 <= note <= 20:
            notes.append(note)
            somme_notes += note
            break
        else:
            print("Note invalide. Veuillez entrer une note entre 0 et 20.")
moyenne = somme_notes / nombreEtudiants
print(f"\nMoyenne de classe : {moyenne:.2f}")
print("\nNuméro de l’Etudiant | note | ecart à la moyenne")
for i, note in enumerate(notes):
    ecart = note - moyenne
    print(f"{i} | {note:.1f} | {ecart:.2f}")
