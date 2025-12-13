"""ce programme permet d'additionner deux nombre et de lever une erreur si l'utilisateur entre une valeur qui n'est pas un entier"""

print("Entrez deux nombre à additionner")
print("Entrez 'q' pour quitter")


while True:
    first = input("Entre le premier nombre: ")
    if first == "q":
        break
    second = input("Entre le deuxieme nombre: ")
    if second == "q":
       break
    try:
        first_num=int(first)
        second_num =int(second)
    except ValueError:
        print("L'une des valeurs saisi n'est pas un entier, veuillez ressayer")
    else:
        print(first_num+second_num)
        print("Saisissez 'q' pour quitter")
print("Merci d'avoir utiliser addition master")