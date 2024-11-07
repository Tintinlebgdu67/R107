while True:
    date = input("Entrez une date sous la forme jjmmaaaa  : ")

    if date.lower() == 'quit':
        print("Fin du programme.")
        break
    if len(date) != 8 or not date.isdigit():
        print("Format incorrect. La date doit être sous la forme jjmmaaaa.")
        continue

    jour = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])
    if mois < 1 or mois > 12:
        print("Mois invalide. Le mois doit être entre 01 et 12.")
        continue

    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        jours_par_mois[1] = 29

    if jour < 1 or jour > jours_par_mois[mois - 1]:
        print(f"Jour invalide pour le mois {mois}.")
        continue

    print("Date valide.")
    print("-" * 40)
