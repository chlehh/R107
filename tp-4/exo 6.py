

def tri_personnalise(tab):
    n = len(tab)
    for i in range(n):
        for j in range(i + 1, n):
            if tab[j] < tab[i]:
                tab[i], tab[j] = tab[j], tab[i]
        print(tab)

tab = [5, 2, 4, 8, 1, 3]

tri_personnalise(tab)

print(sorted(tab))
print(tab)
tab.sort()
print(tab)
