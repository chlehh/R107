
x = int(input("votre nombre =  "))

if x%2==0 :
    x_parite = "paire"
else:
    x_parite = "impaire"
if x>0 :
    x_p = "positif"
else:
    x_p = "négatif"
if x==0 :
    print("Le nombre est zéro (et il est pair)")
else:
    print("le nombre est",x_p," et ",x_parite,)




