def decompose_monnaie(somme):

    billets_100 = somme // 100
    somme %= 100

    billets_50 = somme // 50
    somme %= 50

    billets_10 = somme // 10
    somme %= 10

    pieces_2 = somme // 2
    somme %= 2

    pieces_1 = somme

    print(f"{initial} euros, c'est donc {billets_100} billets de 100, {billets_50} billets de 50, "
          f"{billets_10} billets de 10, {pieces_2} pièces de 2 et {pieces_1} pièce(s) de 1.")


somme = int(input("Entrez une somme d'argent en euros : "))


initial = somme

decompose_monnaie(somme)
