nombre = int(input("Entrez un nombre entier: "))
if nombre > 0:
    print("Le nombre est positif")
elif nombre < 0:
    print("Le nombre est négatif")
else:
    print("Le nombre est nul")
if nombre % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")
