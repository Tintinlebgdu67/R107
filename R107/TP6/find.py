import os
import argparse

def recherche(dossier, fichier, listeFichiers, listeDossiers):
    try:
        liste = os.listdir(dossier)
    except PermissionError:
        print(f"Erreur : Permission refusée pour accéder à {dossier}.")
        return

    for elt in liste:
        chemin_complet = os.path.join(dossier, elt)
        if os.path.isdir(chemin_complet):
            listeDossiers.append(chemin_complet)
            recherche(chemin_complet, fichier, listeFichiers, listeDossiers)
        elif os.path.isfile(chemin_complet):
            if fichier in elt:
                listeFichiers.append(chemin_complet)

def main():
    parser = argparse.ArgumentParser(description="Recherche un fichier dans un dossier et ses sous-dossiers.")
    parser.add_argument("-d", "--dossier", required=True, help="Le dossier à explorer")
    parser.add_argument("-f", "--fichier", required=True, help="Le fichier à rechercher")

    args = parser.parse_args()

    dossier = args.dossier
    fichier = args.fichier
    listeFichiers = []
    listeDossiers = []

    if not os.path.exists(dossier):
        print(f"Erreur : Le dossier '{dossier}' n'existe pas.")
        return

    if not os.path.isdir(dossier):
        print(f"Erreur : '{dossier}' n'est pas un dossier.")
        return

    recherche(dossier, fichier, listeFichiers, listeDossiers)

    for f in listeFichiers:
        print(f)

if __name__ == "__main__":
    main()
