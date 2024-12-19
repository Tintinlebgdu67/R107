#exo chiffre pyramide:
def triangle_isocele(n):
    for i in range(1, n +1):
        for j in range (1, i +1):
            print(j, end=" ")
        print()
    print()
    #affiche triange inversé
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end =" ")
        print()


def main():
    while True:
        try:
            n = int(input("Merci de saisir un nombre dans le type : "))
            triangle_isocele(n)
            break
        except ValueError:
            print("Erreur : veuillez entrez un nombre valide")

main()