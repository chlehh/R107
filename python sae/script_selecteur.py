from PyQt5.QtWidgets import QApplication, QFileDialog
import sys

def select_directory():
    """
    Ouvre une boîte de dialogue pour sélectionner un répertoire.
    Retourne le chemin du répertoire sélectionné.
    """
    app = QApplication(sys.argv)
    directory = QFileDialog.getExistingDirectory(None, "Sélectionnez un répertoire")
    app.exit()
    return directory

if __name__ == "__main__":
    selected_directory = select_directory()
    if selected_directory:
        print(selected_directory)  # Affiche le chemin pour que PowerShell ou un autre script puisse le capturer
    else:
        print("")  # Retourne une chaîne vide si aucun répertoire n'est sélectionné
