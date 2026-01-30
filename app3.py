from model.classroom import Classroom
from model.sutdent import Student

oop = Classroom("OOP")  
oop.add_student(Student(1, "Alice", 20, "P123", "S001"))
oop.add_student(Student(2, "Bob", 22, "P124", "S002"))
print(f"Classroom {oop.name} has {len(oop)} students.")
oop.add_student(Student(3, "Charlie", 21, "P125", "S003"))
print(len(oop))

for i in range(len(oop)):
    print(oop[i])