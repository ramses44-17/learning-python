class Student:
    """model d'un étudiant"""
    def __init__(self, name, age, degree) -> None:
        self.name = name.title()
        self.age = age
        self.degree = degree
    def revise(self):
        print(f"L'étudiant {self.name} de la {self.degree} révise ses cours")
    def sleep(self):
         print(f"L'étudiant {self.name} dort")
    def entertain(self):
        print(f"L'étudiant {self.name} s'amuse ")


class Geek(Student):
    def __init__(self, name, age, degree):
        super().__init__(name, age, degree)
    def reading(self):
        print(f"{self.name} est entrain de lire un livre")


first_student = Student("amos", 19, "undergraduate")
print(first_student.name)
print(first_student.sleep())
first_geek = Geek("david",19,"")

print(first_geek)