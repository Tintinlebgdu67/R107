nMax = 3
x=0
v1 = []
v2 = []

n = int(input("Entre la taille du vecteur :"))
while n > nMax or n <1 :
    n = int(input(f"\nSize ne peux pas être plus grand que {nMax} ou plus petit que 1. Réessayé correctement :"))

print("Saisie du premier vecteur :")
for i in range(n):
    y=int(input("Entrez la valeur du vecteur 2 :"))
    v2.append(y)

print("Saisie du premier vecteur :")
for i in range(n):
    y=int(input("Entrez la valeur du vecteur 1 :"))
    v1.append(y)

for i in range(n):
    x += v1[1] + v2[1]
print(f"\nSize Le produit scalaire de v1 et v2 est {x}")