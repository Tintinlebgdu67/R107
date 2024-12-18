import sys

def demande_arguments():
    args = input("Veuillez entrer les arguments séparés par un espace : ").split()
    return args

def main():
    if len(sys.argv) == 1:
        arguments = demande_arguments()
    else:
        arguments = sys.argv[1:]

    if len(arguments) == 0:
        print(f"Pas assez d'arguments pour le script '{sys.argv[0]}'")
    else:
        print(f"Nombre d'arguments : {len(arguments)}")
        for i, arg in enumerate(arguments, start=1):
            print(f"Argument {i}: {arg}")

if __name__ == "__main__":
    main()
