class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        """Prints a short introduction about the student."""
        print(f"\nHello, my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")


student1 = Student(name="Sung Jinwoo", age=20, course="Computer Science")
student2 = Student(name="Gojo Satoru", age=22, course="Mathematics")
student3 = Student(name="Sung Jinah", age=21, course="Physics")


student1.introduce()
student2.introduce()
student3.introduce()
