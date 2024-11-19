etudiant1 = {
    "firstname": "Corentin",
    "name": "FRIEDMANN",
    "promo": 2025,
    "group": 121
}

print(f"Votre nom est {etudiant1['name']}, prénom est {etudiant1['firstname']}, vous faites partie de la promo {etudiant1['promo']} et votre groupe est {etudiant1['group']}.")

print("Les clés du dictionnaire sont :")
for key in etudiant1.keys():
    print(f"- {key}")

print("Les valeurs du dictionnaire sont :")
for value in etudiant1.values():
    print(f"- {value}")

print("Les tuplets du dictionnaire sont :")
for item in etudiant1.items():
    print(f"- {item}")

etudiant2 = {
    "firstname": "mohamed-amine",
    "name": "AANZOUR",
    "promo": 2025,
    "group": 121
}

binome = {
    54786: etudiant1,
    11878: etudiant2
}

print("Les étudiants formant le binôme sont :")
for etudiant_id, etudiant_info in binome.items():
    print(f"- L'étudiant {etudiant_info['name']} {etudiant_info['firstname']} du groupe {etudiant_info['group']}")
