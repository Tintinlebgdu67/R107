while True:  
    # Demander à l'utilisateur de saisir un nombre entier  
    try:  
        N = int(input("Merci de préciser le nombre souhaité : "))  
        break  # Sortir de la boucle si l'entrée est correcte  
    except ValueError:  
        print("Erreur : veuillez entrer un nombre entier.")  

# Afficher le triangle croissant  
for i in range(1, N + 1):  
    for j in range(1, i + 1):  
        print(j, end=" ")  
    print()  # Nouvelle ligne après chaque rangée  

# Afficher le triangle décroissant  
for i in range(N, 0, -1):  
    for j in range(i, 0, -1):  
        print(j, end=" ")  
    print()  # Nouvelle ligne après chaque rangée  