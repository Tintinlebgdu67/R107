# Demande à l'utilisateur de saisir les composants du vecteur V1  
v1_input = input("Merci de saisir les composantes du vecteur V1 : ")  
# Demande à l'utilisateur de saisir les composants du vecteur V2  
v2_input = input("Merci de saisir les composantes du vecteur V2 : ")  

# Fonction pour calculer le produit scalaire  
def produit_scalaire(v1, v2):  
    # Vérifie si les deux vecteurs ont des composants multiples  
    if len(v1) != len(v2):  
        print("Les deux vecteurs ne sont pas de même taille.")  
        return -2  # Renvoie -2 si les tailles sont différentes  

    # Calcul du produit scalaire  
    produit = sum(a * b for a, b in zip(v1, v2))  
    return produit  

# Fonction pour traiter l'entrée utilisateur  
def traiter_entree(vecteur_input):  
    # Sépare les composants par virgule et les convertit en entiers  
    try:  
        vecteur = list(map(int, vecteur_input.split(',')))  
        return vecteur  
    except ValueError:  
        print("Erreur : assurez-vous d'utiliser des nombres entiers séparés par des virgules.")  
        return None  # Renvoie None en cas d'erreur de conversion  

# Traitement des entrées  
v1 = traiter_entree(v1_input)  
v2 = traiter_entree(v2_input)  

# Vérifie si les entrées sont valides avant de calculer le produit scalaire  
if v1 is not None and v2 is not None:  
    if len(v1) == 1 or len(v2) == 1:  
        print("Un des deux vecteurs est composé d'une seule composante.")  
        print("Veuillez utiliser le séparateur correct (virgule).")  
        print(-1)  # Renvoie -1 si un vecteur a une seule composante  
    else:  
        result = produit_scalaire(v1, v2)  
        if result != -2:  # Vérifie si les vecteurs sont de même taille  
            print(f"Le produit scalaire de V1 par V2 vaut {result}.")