"""
demande à l'utilisateur son nom
"""
from pathlib import Path

name = input("Veuillez entrer votre nom: ")
path = Path("user_name.txt")
path.write_text(name)
