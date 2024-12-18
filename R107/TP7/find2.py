import os

def recherche(dossier):
    listeFichiers = []
    listeDossiers = []

    try:
        liste = os.listdir(dossier)
    except PermissionError:
        print(f"Erreur : Permission refusée pour accéder à {dossier}.")
        return [], []

    for elt in liste:
        chemin_complet = os.path.join(dossier, elt)
        if os.path.isdir(chemin_complet):
            listeDossiers.append(chemin_complet)
            sous_dossiers, sous_fichiers = recherche(chemin_complet)
            listeDossiers.extend(sous_dossiers)
            listeFichiers.extend(sous_fichiers)
        elif os.path.isfile(chemin_complet):
            listeFichiers.append(chemin_complet)

    return listeDossiers, listeFichiers

def main():
    dossier = input("Veuillez entrer le chemin du dossier à explorer : ")

    if not os.path.exists(dossier):
        print(f"Erreur : Le dossier '{dossier}' n'existe pas.")
        return

    if not os.path.isdir(dossier):
        print(f"Erreur : '{dossier}' n'est pas un dossier.")
        return

    listeDossiers, listeFichiers = recherche(dossier)

    print("\nListe des dossiers trouvés :")
    for d in listeDossiers:
        print(d)

    print("\nListe des fichiers trouvés :")
    for f in listeFichiers:
        print(f)

if __name__ == "__main__":
    main()
