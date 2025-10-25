from os import listdir
from os.path import isfile, join
def printFiles(dir):
    for file_or_folder in sorted(listdir(dir)):
        element_to_check = join(dir, file_or_folder)
        if isfile(element_to_check):
            print(file_or_folder)
        else:
            printFiles(element_to_check)


printFiles(dir = "learning-python")