def make_sandwich(*ings):
    """Affiche les ingrédients d'un sandwich commandé."""
    if not list(ings):
        print("Aucun ingredient spécifié")
    else:
        print("Vous avez commandé un sandwich aux ingredients suivant: ")
        for ing in ings:
            print(f'- {ing}')

# appel de la fonction avec différents ingrédients trois fois
make_sandwich('jambon', 'fromage', 'laitue')
make_sandwich('poulet', 'tomate', 'mayonnaise', 'fromage')
make_sandwich()  # appel sans ingrédients
make_sandwich('thon', 'oeuf', 'cresson', 'avocat', 'moutarde')