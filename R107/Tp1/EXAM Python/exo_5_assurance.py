
def assurance(age,annee, nbr_accident,anciennete):
    annee_courante= 2024
    
    #verification des conditions 
    if nbr_accident < 0 or nbr_accident < 0:
        return "Anomalie"
    if age < 16:
        return "rouge"
    if annee > annee_courante:
        return "Anomalie"
    if annee < 16:
        return "Anomalie"

    #verification des tarifs de l'assurance
    if  (age < 25 and anciennete >= 2) or (age >= 25 and anciennete < 2):
        if nbr_accident ==0:
            return "orange"
        elif nbr_accident > 0:
            return "rouge"
    elif age < 25 and nbr_accident > 0:
        return "rouge"
    elif age >=25:
        if anciennete < 2:
            return "Rouge"
        if nbr_accident == 0:
            return "Bleu"
        if nbr_accident > 0:
            return "orange"
    elif anciennete > 1:
        if nbr_accident == 0:
            return "Vert"
        elif nbr_accident > 0:
            return "orange"
    else:
        print("entrez une valeur valide !")


print(assurance(23, 2022, 0, 0))
    
