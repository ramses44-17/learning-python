"""Compte le nombre approximatif des mots d'un fichier text"""
from pathlib import Path

def count_word(filepath):
    path = Path(filepath)
    try:
        content = path.read_text("utf-8")
    except FileNotFoundError:
        print(f"Fichier {path} non trouvé")
    else:
        num_word = len(content.split())
        print(f"Le fichier {path} a approximativement {num_word} mots")


filenames = ["pi.txt","user_name.txt","bbb.tx","user_names.txt","programming.txt","pg84.txt"]

for filename in filenames:
    count_word(filename)