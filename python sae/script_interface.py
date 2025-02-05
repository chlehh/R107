from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QPushButton, QCheckBox, QLabel, QHBoxLayout
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QColor
import json
import sys
import random
NB_LEGENDES_PAR_PAGE = 25

class FenetrePrincipale(QMainWindow):
    def __init__(self, fichiers):
        super().__init__()
        self.fichiers = fichiers
        self.cases_a_cocher = []
        self.couleurs_fichiers = {}  # Dictionnaire pour stocker les couleurs

        self.setWindowTitle("Résultat de recherche des 'gros' fichiers")
        self.setGeometry(200, 100, 1000, 700)

        # Création des onglets
        self.onglets = QTabWidget()
        self.setCentralWidget(self.onglets)

        # Ajout des onglets
        if self.fichiers:
            self.afficher_camembert()
            self.afficher_legendes()
        else:
            self.afficher_message_aucun_fichier()

        self.afficher_bouton_suppression()

    def afficher_legendes(self):
     for i in range(0, len(self.fichiers), NB_LEGENDES_PAR_PAGE):
        tab = QWidget()
        layout = QVBoxLayout()
        
        for fichier in self.fichiers[i:i + NB_LEGENDES_PAR_PAGE]:
            chemin, taille = fichier
            taille_mo = taille // 1048576
            
            ligne_layout = QHBoxLayout()
            ligne_layout.setSpacing(5)
            
            case_a_cocher = QCheckBox()
            self.cases_a_cocher.append((case_a_cocher, chemin))
            
            texte_legende = QLabel(f"<span style='color:black;'>{chemin}</span> --> <span style='color:red;'>{taille_mo} Mo</span>")
            
            ligne_layout.addWidget(case_a_cocher)
            ligne_layout.addWidget(texte_legende)
            layout.addLayout(ligne_layout)
        
        tab.setLayout(layout)
        self.onglets.addTab(tab, f"Légendes {i // NB_LEGENDES_PAR_PAGE + 1}")

    def afficher_camembert(self):
        """Ajoute un onglet avec un graphique de type camembert."""
        tab = QWidget()
        layout = QVBoxLayout()
        series = QPieSeries()
        total_size = sum(fichier[1] for fichier in self.fichiers)
        for fichier in self.fichiers:
            chemin, taille = fichier
            taille_mo = taille // 1048576  
            pourcentage = (taille / total_size) * 100

            
            couleur = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.couleurs_fichiers[chemin] = couleur  

            # Conditions pour afficher ou non l'étiquette
            label_text = f"{taille_mo} Mo ({pourcentage:.2f}%)" if pourcentage > 5 else ""

            slice_ = series.append(label_text, pourcentage)
            slice_.setBrush(couleur)
            slice_.setLabelVisible(pourcentage > 5)  # Affiche seulement si > 5%

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Répartition des tailles des fichiers")
        chart.legend().hide()

        chart_view = QChartView(chart)
        layout.addWidget(chart_view)
        tab.setLayout(layout)
        self.onglets.addTab(tab, "Camembert")

    def afficher_legendes(self):
        """Ajoute un onglet pour afficher les légendes avec cases à cocher et noms côte à côte."""
        tab = QWidget()
        layout = QVBoxLayout()

        for fichier in self.fichiers:
            chemin, taille = fichier
            taille_mo = taille // 1048576

            case_a_cocher = QCheckBox()
            case_a_cocher.setText(f"{chemin} --> {taille_mo} Mo")
            case_a_cocher.setStyleSheet(f"color: rgb({self.couleurs_fichiers[chemin].red()}, {self.couleurs_fichiers[chemin].green()}, {self.couleurs_fichiers[chemin].blue()});")
            self.cases_a_cocher.append((case_a_cocher, chemin))

            ligne_layout = QHBoxLayout()
            ligne_layout.addWidget(case_a_cocher)
            layout.addLayout(ligne_layout)

        tab.setLayout(layout)
        self.onglets.addTab(tab, "Légendes")

    def afficher_message_aucun_fichier(self):
        """Ajoute un onglet avec un message indiquant qu'aucun fichier n'a été trouvé."""
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Aucun fichier volumineux trouvé dans le répertoire sélectionné.")
        layout.addWidget(label)
        tab.setLayout(layout)
        self.onglets.addTab(tab, "Aucun fichier")

    def afficher_bouton_suppression(self):
        """Ajoute un onglet avec un bouton pour générer le script PowerShell."""
        tab = QWidget()
        layout = QVBoxLayout()

        bouton = QPushButton("Générer le script PowerShell de suppression")
        bouton.clicked.connect(self.generer_script_suppression)
        layout.addWidget(bouton)

        tab.setLayout(layout)
        self.onglets.addTab(tab, "IHM")

    def generer_script_suppression(self):
        """Génère un script PowerShell pour supprimer les fichiers sélectionnés."""
        fichiers_a_supprimer = [chemin for case, chemin in self.cases_a_cocher if case.isChecked()]

        if fichiers_a_supprimer:
            with open("script_suppression.ps1", "w") as script:
                script.write('Write-Output "Script PowerShell pour supprimer des fichiers sans confirmation"\n')
                script.write('Write-Output "Attention : cette suppression est définitive..."\n\n')
                script.write('$reponse = Read-Host "Confirmez la suppression : (OUI)"\n')
                script.write('if ($reponse -eq "OUI") {\n')
                for fichier in fichiers_a_supprimer:
                    script.write(f'    Remove-Item -Path "{fichier}" -Force\n')
                script.write('}\n')
            print("Script de suppression généré : script_suppression.ps1")
        else:
            print("Aucun fichier sélectionné pour la suppression.")

if __name__ == "__main__":
    # Lecture des fichiers JSON
    nom_fichier_json = "resultats_gros_fichiers.json"
    try:
        with open(nom_fichier_json, "r") as fichier_json:
            fichiers = json.load(fichier_json)
    except FileNotFoundError:
        fichiers = []
        print(f"Fichier JSON '{nom_fichier_json}' introuvable.")
    except json.JSONDecodeError:
        fichiers = []
        print(f"Erreur lors de la lecture du fichier JSON '{nom_fichier_json}'.")

    # Création de l'application graphique
    app = QApplication(sys.argv)
    fenetre = FenetrePrincipale(fichiers)
    fenetre.show()
    sys.exit(app.exec_()) 