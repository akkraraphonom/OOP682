from model.person import Person

class staff(Person):
    def __init__(self, name, age, pid, staff_id):
        super().__init__(name, age , pid)
        self.staff_id = staff_id

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    