# Lancement du script pour sélectionner le répertoire
$rep_base = python "script_selecteur.py"
if (-not $rep_base) {
    Write-Output "Aucun répertoire sélectionné. Fin du script."
    exit
}

# Lancement du script d'analyse
python "script_analyse.py" --rep_base $rep_base

# Lancement de l'interface graphique
python "script_interface.py"
