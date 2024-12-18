import unicodedata
import re


def nettoyer_texte(texte):
    texte_nettoye = re.sub(r'[^a-zA-Z0-9]', '', texte)
    return texte_nettoye.lower()

def supprimer_accents(texte):

    texte_sans_accents = unicodedata.normalize('NFD', texte)
    texte_sans_accents = ''.join(
        c for c in texte_sans_accents if unicodedata.category(c) != 'Mn')
    return texte_sans_accents



def est_palindrome(texte):
    texte_nettoye = nettoyer_texte(texte)
    texte_sans_accents = supprimer_accents(texte_nettoye)
    return texte_sans_accents == texte_sans_accents[::-1]


def main():
    texte = input("Entrez un mot ou une phrase : ")
    if est_palindrome(texte):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")
if __name__ == "__main__":
    main()
