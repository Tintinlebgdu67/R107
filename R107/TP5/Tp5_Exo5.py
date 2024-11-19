def calculer_salaire(heures_travaillees, salaire_horaire):

    heures_normales = min(heures_travaillees, 160)
    salaire = heures_normales * salaire_horaire


    if heures_travaillees > 160:
        heures_sup_25 = min(heures_travaillees - 160, 40)
        salaire += heures_sup_25 * salaire_horaire * 1.25

    if heures_travaillees > 200:
        heures_sup_50 = heures_travaillees - 200
        salaire += heures_sup_50 * salaire_horaire * 1.5

    return salaire

heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire = calculer_salaire(heures_travaillees, salaire_horaire)

print(f"Le salaire pour {heures_travaillees} heures travaillées est : {salaire:.2f} euros.")
