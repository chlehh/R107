
def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

print(ajouter_elt())

print(ajouter_elt())

def ajouter_elt(lst=[0, 1, 2], elt=3):
    print("ID de lst avant ajout:", id(lst))
    lst.append(elt)
    print("ID de lst après ajout:", id(lst))
    return lst

ajouter_elt()

ajouter_elt()

def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

print(ajouter_carac())

ajouter_carac()
ajouter_carac()

