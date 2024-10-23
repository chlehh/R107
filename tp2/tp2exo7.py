import random
biais_pour_pile= 3/2
if random.randint(0,100) < 50*biais_pour_pile :
    print("Pile !!")
else:
    print("Face !! ")