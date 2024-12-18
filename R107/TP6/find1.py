import os


def aide():
    print("Erreur: Vous devez fournir un chemin de dossier valide.")
    print("Usage : python find1.py <chemin_du_dossier>")
    print("Le chemin du dossier doit être un dossier existant sur votre système.")


def affiche(dossier):
    try:
        for fichier in os.listdir(dossier):
            print(fichier)
    except PermissionError:
        print(f"Erreur : Permission refusée pour accéder à {dossier}.")
    except Exception as e:
        print(f"Erreur : {str(e)}")


def main():
    dossier = input("Veuillez entrer le chemin du dossier à explorer : ")

    if not os.path.exists(dossier):
        print(f"Erreur : Le dossier '{dossier}' n'existe pas.")
        return

    if not os.path.isdir(dossier):
        print(f"Erreur : '{dossier}' n'est pas un dossier.")
        return

    affiche(dossier)


if __name__ == "__main__":
    main()
