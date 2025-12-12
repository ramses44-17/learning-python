from pathlib import Path

path = Path("pi.txt")
content = path.read_text().rstrip()
# print(__file__)
for line in content.splitlines():
    print(line)