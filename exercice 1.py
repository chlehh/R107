
L1 = [0]*3
print("a) Liste initiale :", L1)
print("Type de la liste :", type(L1))
print("ID de la liste :", id(L1))

print("\nb) Valeur, type et ID de chaque élément de la liste :")
for element in L1:
    print(f"Valeur: {element}, Type: {type(element)}, ID: {id(element)}")

L1[1] += 1
print("\nc) Liste après modification :", L1)
print("Type de la liste après modification :", type(L1))
print("ID de la liste après modification :", id(L1))

print("\nd) Valeur, type et ID de chaque élément après modification :")
for element in L1:
    print(f"Valeur: {element}, Type: {type(element)}, ID: {id(element)}")


chaine = "machaine"
print("\ne) ID de la chaîne :", id(chaine))
for char in chaine:
    print(f"Caractère: {char}, Type: {type(char)}, ID: {id(char)}")