# classes.py

class Student:
    # Class variable
    school = "ABC School"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school)


# Inheritance
class Monitor(Student):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def show_monitor(self):
        self.display()
        print("Section:", self.section)


# Object creation
s1 = Student("Ali", 20)
s1.display()

print()

m1 = Monitor("Ahmed", 22, "A")
m1.show_monitor()