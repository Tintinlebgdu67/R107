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

#exo produit scalaire

def produit_scalaire():
    v1 = input("Merci de saisir les composantes du vecteur V1 (séparé par des virgules): ")
    v2 = input("Merci de saisir les composantes du vecteur V1 (séparé par des virgules): ")

    try: 
        vecteur1 = [float(x)] for x in v1.split(",")]:
        vecteur2 = [float(x)] for x in v1.split(",")]:
        if len (vecteur1) != len(vecteur2):
            return "les vecteurs ne sont pas de la même taille "
        #calcul du produit scalaire :
        produit = sum(a*b for a, b in zip(vecteur1, vecteur2))
        return f"leproduit scalaire de V1 et V2 vaut {produit}"
    except ValueError:
        return "erreur : veuillez entrez des nombre valides séparé d'une la virgule"

Resultat = produit_scalaire()
print(Resultat)
