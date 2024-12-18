def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]

lst2 = ajouter_elt(lst1, len(lst1))

print("Liste lst1:")
print("Contenu:", lst1)
print("Type:", type(lst1))
print("Identifiant:", id(lst1))

print("\nListe lst2:")
print("Contenu:", lst2)
print("Type:", type(lst2))
print("Identifiant:", id(lst2))
