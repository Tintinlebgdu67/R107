y = 1
z = 1
loop = 0
mult = 1
x = int(input("Entrez une valeur : "))

for i in range(x):
    y = y * mult
    mult += 1

while loop < x:
    loop = loop + 1
    z = z * loop

print("Pour la boucle :",y)
print("Tant que la boucle : ",z)