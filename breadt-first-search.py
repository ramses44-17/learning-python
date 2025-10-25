# analyser le repertoire en cours s'il trouve un fichier il affcihe
# si c'est un dossier il cherche dedans
from os import listdir
from collections import deque
from os.path import isfile, join


def printFiles(dir):
    folder_queu = deque()
    folder_queu.append(dir)
    while folder_queu:
        folder_to_check = folder_queu.popleft()
        for file_or_folder in sorted(listdir(folder_to_check)):
            element_to_check = join(folder_to_check, file_or_folder)
            if isfile(element_to_check):
                print(file_or_folder)
            else:
                folder_queu.append(element_to_check)

printFiles(dir = "learning-python")
