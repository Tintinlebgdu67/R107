nb_ligne = int(input("Merci de préciser le nombre de ligne : "))
l = 0
for i in range(nb_ligne, 0 , -1):  
    print("*", end=" ")  
    print("\n")
print("premiere possibilité")

#print("*", end=" \n")

N = 0
for i in range(0, nb_ligne + 1 , 1): 
    N =i * "* "
    print(N, sep=" ")
print("Voici le premier triangle isocèle")

N = 0
decalage = " "
for i in range(nb_ligne , 0 , -1): 
    N =i * "* "
    decalage = i * decalage
    print(decalage, N)
print("Voici le second triangle isocèle")


#Exercice table de mutliplication : 

Nombre = float(input("Vous cherchez la table de multiplication de quel nombre ?"))
Resultat = 1
for i in range (0, 11, 1):
    Resultat = Nombre * i
    print(f"{Nombre} * {i} = {round(Resultat, 1)}")



def tabl_multi():
    resultats = []  
    for i in range(10):  
        resultat = round(nombre * i, 1)  # Multiplication arrondie à 1 décimale  
        resultats.append(f"{nombre} * {i} = {resultat}")  # Formatage du résultat  
    return resultats  
    return L
nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
print(f"Voici la table de mutliplication de {nombre}")  

def affich_table(L):



#exo produit scalaire

def produit_scalaire():
    v1 = input("Merci de saisir les composantes du vecteur V1 (séparé par des virgules): ")
    v2 = input("Merci de saisir les composantes du vecteur V1 (séparé par des virgules): ")

    try: 
        vecteur1 = [float(x)] for x in v1.split(",")]
        vecteur2 = [float(x)] for x in v1.split(",")]
        if len (vecteur1) != len(vecteur2):
            return "les vecteurs ne sont pas de la même taille "
        #calcul du produit scalaire :
        produit = sum(a*b for a, b in zip(vecteur1, vecteur2))
        return f"leproduit scalaire de V1 et V2 vaut {produit}"
    except ValueError:
        return "erreur : veuillez entrez des nombre valides séparé d'une la virgule"

Resultat = produit_scalaire()
print(Resultat)



#exo chiffre pyramide:
def triangle_isocele(n):
    for i in range(1, n +1):
        for j in range (1, i +1):
            print(j, end=" ")
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