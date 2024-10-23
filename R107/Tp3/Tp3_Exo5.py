def calculer_prix_location(debut, fin):

    if debut < 0 or debut > 24 or fin < 0 or fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !")
        return
    if debut == fin:
        print("L’heure de fin est identique à l’heure de début.")
        return
    if debut > fin:
        print("L’heure de début de la location est après la fin.")
        return


    prix = 0
    for heure in range(debut, fin):
        if (0 <= heure < 7) or (17 <= heure < 24):
            prix += 1
        elif 7 <= heure < 17:
            prix += 2

    print(f"{prix} euros")



try:
    debut = int(input("Entrez l'heure de début de location (entre 0 et 24) : "))
    fin = int(input("Entrez l'heure de fin de location (entre 0 et 24) : "))
    calculer_prix_location(debut, fin)
except ValueError:
    print("Veuillez entrer des nombres entiers.")
