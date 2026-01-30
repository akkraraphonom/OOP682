from model.person import Person

class student(Person):
    def __init__(self, name, age, pid, student_id):
        super().__init__(name, age , pid)
        self.st5udent_id = student_id
        
    def __str__(self):
        return f"{self.name} is {self.age} years old."