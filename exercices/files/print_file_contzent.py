from pathlib import Path
path = Path("pi.txt")
try:
    content = path.read_text().rstrip()
except FileNotFoundError:
    print("Le fichier n'est pas trouvé dans le chemin specifié")
else:
    for line in content.splitlines():
        print(line)