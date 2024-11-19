notes = []
coefficients = []

for i in range(1, 6):
    saisie = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    note, coefficient = saisie.split()
    notes.append(float(note))
    coefficients.append(int(coefficient))

somme_ponderation = sum(note * coef for note, coef in zip(notes, coefficients))
somme_coefficients = sum(coefficients)

moyenne = somme_ponderation / somme_coefficients

admis = all(note >= 8 for note in notes)

print(f"\nMoyenne générale : {moyenne:.2f}")
if moyenne > 10 and admis:
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")
