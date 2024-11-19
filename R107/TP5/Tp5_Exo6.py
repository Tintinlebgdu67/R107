def calculer_taille(chaine):

    taille = 0
    for char in chaine:
        taille += 1
    return taille

def calculer_pourcentage_voyelles(chaine):

    voyelles = "aeiouAEIOU"
    nombre_voyelles = 0
    taille = 0
    for char in chaine:
        if char != ' ':
            taille += 1
            if char in voyelles:
                nombre_voyelles += 1
    if taille == 0:
        return 0
    return (nombre_voyelles / taille) * 100

def chercher_sous_chaine(chaine, sous_chaine):

    n = len(chaine)
    m = len(sous_chaine)
    for i in range(n - m + 1):
        if chaine[i:i + m] == sous_chaine:
            return i
    return -1

def compter_occurrences(chaine, sous_chaine):

    n = len(chaine)
    m = len(sous_chaine)
    count = 0
    for i in range(n - m + 1):
        if chaine[i:i + m] == sous_chaine:
            count += 1
    return count


chaine = input("Entrez une chaîne de caractères : ")


taille = calculer_taille(chaine)
print(f"La taille de la chaîne est : {taille}")


pourcentage_voyelles = calculer_pourcentage_voyelles(chaine)
print(f"Le pourcentage de voyelles dans la chaîne est : {pourcentage_voyelles:.2f}%")


sous_chaine = "wagon"
indice = chercher_sous_chaine(chaine, sous_chaine)
if indice != -1:
    print(f"Le mot 'wagon' est une sous-chaîne, et il commence à l'indice {indice}.")
else:
    print("Le mot 'wagon' n'est pas une sous-chaîne.")


occurrences = compter_occurrences(chaine, sous_chaine)
print(f"Le mot 'wagon' apparaît {occurrences} fois dans la chaîne.")
