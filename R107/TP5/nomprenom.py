prenom1 = input("Entrez le prénom de la première personne : ")
nom1 = input("Entrez le nom de la première personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")
nom2 = input("Entrez le nom de la deuxième personne : ")

prenom1 = prenom1.capitalize()
nom1 = nom1.upper()
prenom2 = prenom2.capitalize()
nom2 = nom2.upper()  # Nom en majuscules

if nom1 < nom2 or (nom1 == nom2 and prenom1 < prenom2):
    print(f"{prenom1} {nom1}")
    print(f"{prenom2} {nom2}")
else:
    print(f"{prenom2} {nom2}")
    print(f"{prenom1} {nom1}")
