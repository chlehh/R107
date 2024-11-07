def table_multiplication(nombre):
    table = []
    for i in range(10):
        result = round(nombre * i, 2)
        table.append(result)
    print(f"Vous cherchez la table de multiplication de quel nombre ?")
    for i, result in enumerate(table):
        print(f"{nombre} * {i} = {result}")
nombre = float(input("Entrez un nombre réel : "))
table_multiplication(nombre)
