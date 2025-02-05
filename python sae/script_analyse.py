import json
import argparse
from pathlib import Path

def analyse_repertoire(repertoire_de_base):
   
    fichiers = []
    for fichier in Path(repertoire_de_base).rglob("*"):
        if fichier.is_file():
            print(f"Chemin analysé : {fichier.resolve()}")  
            fichiers.append([str(fichier.resolve()), fichier.stat().st_size])
    return fichiers

def trier_fichiers_par_taille(fichiers):
    """
    Trie une liste de fichiers par taille décroissante.
    """
    return sorted(fichiers, key=lambda x: x[1], reverse=True)

def filtrer_fichiers(fichiers, taille_min_mo, taille_max_mo, nb_max_fichiers):
    """
    Filtre les fichiers en fonction de leur taille minimale et maximale (en Mo) 
    et du nombre maximum à conserver.
    """
    taille_min_octets = taille_min_mo * 1048576  # Conversion Mo -> octets
    taille_max_octets = taille_max_mo * 1048576  # Conversion Mo -> octets
    fichiers_filtres = [
        fichier for fichier in fichiers
        if taille_min_octets <= fichier[1] <= taille_max_octets
    ]
    print(f"Nombre de fichiers après filtrage : {len(fichiers_filtres)}")  # Vérification
    return fichiers_filtres[:nb_max_fichiers]

def sauvegarder_en_json(fichiers, nom_fichier_json):
    """
    Sauvegarde une liste de fichiers dans un fichier JSON.
    """
    print(f"Fichiers sauvegardés dans le JSON : {fichiers}")  # Affichage du contenu sauvegardé
    for fichier in fichiers:
        fichier[0] = fichier[0].replace("\\", "\\\\")  # Double antislash pour Windows
    with open(nom_fichier_json, "w") as fichier_json:
        json.dump(fichiers, fichier_json, indent=4)

if __name__ == "__main__":
    # Ajout des arguments pour le chemin et les paramètres
    parser = argparse.ArgumentParser(description="Analyse des fichiers d'un répertoire.")
    parser.add_argument("--rep_base", required=True, help="Chemin du répertoire de base à analyser")
    parser.add_argument("--taille_min", type=float, default=1, help="Taille minimale des fichiers en Mo (par défaut 1 Mo)")
    parser.add_argument("--taille_max", type=float, default=float("inf"), help="Taille maximale des fichiers en Mo (par défaut illimité)")
    parser.add_argument("--nb_max", type=int, default=100, help="Nombre maximum de fichiers à conserver (par défaut 100)")

    args = parser.parse_args()
    repertoire_de_base = args.rep_base
    taille_min_mo = args.taille_min
    taille_max_mo = args.taille_max
    nb_max_fichiers = args.nb_max

    # Étape 1 : Analyse des fichiers
    fichiers = analyse_repertoire(repertoire_de_base)

    # Étape 2 : Tri des fichiers
    fichiers_tries = trier_fichiers_par_taille(fichiers)

    # Étape 3 : Filtrage des fichiers
    fichiers_filtres = filtrer_fichiers(fichiers_tries, taille_min_mo, taille_max_mo, nb_max_fichiers)

    # Étape 4 : Sauvegarde dans un fichier JSON
    nom_fichier_json = "resultats_gros_fichiers.json"
    sauvegarder_en_json(fichiers_filtres, nom_fichier_json)

    print(f"Analyse terminée. Résultats sauvegardés dans {nom_fichier_json}.")
