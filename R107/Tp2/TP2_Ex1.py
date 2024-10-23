x = int(input("Entrez x: "))
y = int(input("Entrez y: "))
print(f"Avant permutation:\nx : {x}\ny : {y}")
x, y = y, x
print(f"Après permutation:\nx : {x}\ny : {y}")