def est_palindrome(chaine):

    chaine = chaine.lower()

    chaine_sans_non_alphab = ''.join(c for c in chaine if c.isalpha())

    return chaine_sans_non_alphab == chaine_sans_non_alphab[::-1]

chaine = input("Entrez un mot ou une phrase : ")

if est_palindrome(chaine):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
