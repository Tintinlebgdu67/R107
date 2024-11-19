login1 = input("Entrez votre login: ")
login2 = input("Voisin entrez votre login: ")

binome = (login1, login2)

print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")


# Les tuplets ne peuvent pas être modifié

# del() binome[1] ne fonctionne il y a une erreur
login3= input("Entre le login du dernier voisin :")
binome = binome + ("login3",)

print(f"L’étudiant {binome[0]} est en binôme avec l’étudiant {binome[1]} et {binome[2]}")
