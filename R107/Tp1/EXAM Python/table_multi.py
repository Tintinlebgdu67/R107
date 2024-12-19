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