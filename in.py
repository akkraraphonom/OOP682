class Person:
    def __init__(self, name, age , pid):
        self.name = name
        self.age = age
        self.pid = pid
    def __str__(self):
        return f"{self.name} is {self.age} years old."

class student(Person):
    def __init__(self, name, age, pid, student_id):
        super().__init__(name, age , pid)
        self.st5udent_id = student_id
    def __str__(self):
        return f"{self.name} is {self.age} years old."

class staff(Person):
    def __init__(self, name, age, pid, staff_id):
        super().__init__(name, age , pid)
        self.staff_id = staff_id
    def __str__(self):
        return f"{self.name} is {self.age} years old."

def get_person_info(person):
    print(isinstance(person, Person))
    return f"Name: {person.name}, Age: {person.age}, PID: {person.pid}"


student1 = student("Alice", 20, "P123", "S456")
staff1 = staff("Bob", 35, "P789", "ST101")
print(f"Student Name: {student1.name}, Age: {student1.age}, PID: {student1.pid}, Student ID: {student1.st5udent_id}")
print(f"Staff Name: {staff1.name}, Age: {staff1.age}, PID: {staff1.pid}, Staff ID: {staff1.staff_id}")



get_person_info(student1)
get_person_info(staff1)

# class employee:
#     pass

# manager = employee()
# get_person_info(manager)

        