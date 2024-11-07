import time
n = int(input("Veuillez entrer un nombre entier positif : "))
if n < 0:
    print("Le nombre doit être positif.")
else:
    while n >= 0:
        print(n)
        n -= 1
        time.sleep(1)
import time
n = int(input("Veuillez entrer un nombre entier positif : "))
if n < 0:
    print("Le nombre doit être positif.")
else:
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)
