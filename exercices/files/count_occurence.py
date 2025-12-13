from pathlib import Path


"""
Cette fonction compte les occurence d'une chaine dans un fichier texte
il prend en parametre, le chemin du fichier et la chaine à rechercher
il renvoi un dictionnaire dont les clés sont les numeros de ligne où la chaine apparait et les valeurs sont le nombre de fois que la chaine apparait dans cette ligne.
renvoi -1, si le fichier n'existe pas et un dictionnaire vide si le mot 
n'apparait pas.
"""
def count_occurrence(file_path,word):
    path = Path(file_path)
    i=1
    try:
        content = path.read_text("utf-8")
        content_lines = content.splitlines()
        results = {}
    except FileNotFoundError:
        return -1
    else:
            for line in content_lines:
                num = line.lower().count(word)
                if num != 0:
                    results[i] = num
                i+=1
    return results


print(count_occurrence('pg84.txt',"nnn"))


        
# Amélioration

# 1. Lisibilité

# L’utilisation de i pour compter les lignes est correcte, mais moins pythonique que enumerate(content_lines, start=1).

# Les noms de variables peuvent être plus explicites : par exemple line_number au lieu de i, occurrences au lieu de num.

# 2. Robustesse

# La fonction ne gère que FileNotFoundError. D’autres erreurs peuvent survenir :

# Problèmes de lecture (UnicodeDecodeError).

# Chemin invalide ou permissions refusées.

# Actuellement, la fonction ne gère pas la casse : "Hello" et "hello" seront considérés différents.

# La fonction ne gère pas les mots attachés à des ponctuations ("hello!" ne sera pas compté si on cherche "hello").

# 4. Performance

# Lire tout le fichier en mémoire (read_text) peut être problématique pour des fichiers très volumineux.

# Une approche ligne par ligne (open(file)) serait plus efficace pour les gros fichiers.

# 5. Style Python / Best Practices

# Pas d’import visible de Path. La fonction suppose from pathlib import Path.

# Le retour -1 pour fichier introuvable est correct mais pas idiomatique en Python. Il vaudrait mieux lever une exception ou retourner None.

# La fonction peut être écrite de manière plus concise avec des compréhensions de dictionnaire.

# 6. Flexibilité

# Actuellement, la fonction ne permet pas :

# Recherche insensible à la casse.

# Recherche de mots entiers uniquement (pour éviter de compter "the" dans "there").

# Retourner des statistiques globales (total occurrences dans le fichier).