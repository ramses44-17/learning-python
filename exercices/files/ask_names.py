from pathlib import Path

path = Path("user_names.txt")
content = ""
while True:
    name = input("Veuillez entrer un nom(ou 0 si il y'en a plus): ")
    if(name == "0"):
        break
    content+=f"{name}\n"
path.write_text(content)