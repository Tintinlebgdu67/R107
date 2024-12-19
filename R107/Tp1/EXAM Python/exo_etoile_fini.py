
nb_ligne = int(input("Merci de préciser le nombre de ligne : "))
N = 0
print("Le premier triangle isocèle")
for i in range(0, nb_ligne + 1 , 1): 
    N =i * "* "
    print(N, sep=" ")

print("le second triangle isocèle")
for i in range(nb_ligne, 0, -1):
    print(' ' * (nb_ligne - i -1), end=" ")
    print('* ' * (i))
print()
