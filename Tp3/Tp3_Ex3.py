import random

Number = random.randint(0,99)
guess = int(input("Essaye de trouver le nombre exact : "))
count = 1

while guess != Number:
    if Number > guess:
        print("Le nombre est plus grand !")
    elif Number < guess:
        print("Le nombre est plus petit !")
    count += 1
    guess = int(input("\nEssaye encore :"))

print("\nTu as trouvé le bon nombre !")
print("Le nombre était",Number,".")
print("Tu as trouvé en ",count,"essai.")