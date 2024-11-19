import os
import datetime

def afficher_informations_fichier(fichier):

    if os.path.isfile(fichier):
        taille = os.path.getsize(fichier)
        mtime = os.path.getmtime(fichier)
        date_modification = datetime.datetime.fromtimestamp(mtime)
        return taille, date_modification
    else:
        return None, None

def verification_fichiers():

    fichier1 = input("Entrez le nom du premier fichier : ")
    fichier2 = input("Entrez le nom du second fichier : ")


    taille1, date_modif1 = afficher_informations_fichier(fichier1)
    taille2, date_modif2 = afficher_informations_fichier(fichier2)


    if taille1 is not None and taille2 is not None:
        print(f"\nFichier 1: {fichier1}")
        print(f"Taille : {taille1} octets")
        print(f"Date de dernière modification : {date_modif1}")

        print(f"\nFichier 2: {fichier2}")
        print(f"Taille : {taille2} octets")
        print(f"Date de dernière modification : {date_modif2}")


        if date_modif1 > date_modif2:
            print(f"\nLe fichier le plus récent est {fichier1} (modifié le {date_modif1})")
        elif date_modif1 < date_modif2:
            print(f"\nLe fichier le plus récent est {fichier2} (modifié le {date_modif2})")
        else:
            print("\nLes deux fichiers ont été modifiés à la même date.")
    else:
        if taille1 is None:
            print(f"\nLe fichier '{fichier1}' n'existe pas.")
        if taille2 is None:
            print(f"\nLe fichier '{fichier2}' n'existe pas.")


verification_fichiers()
