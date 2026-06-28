print("Student Course Management System(Overall Oops Concept:")
print('-'*30)

from abc import ABC, abstractmethod
class Student(ABC):
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__course = "Python Programming"
    def get_course(self):
        return self.__course
    def set_course(self, course):
        self.__course = course

    @abstractmethod
    def student_type(self):
        pass

class RegularStudent(Student):
    def student_type(self):
        print("\nStudent Type : Regular")
    def display(self):
        self.student_type()
        print("Name      :", self.name)
        print("Roll No   :", self.roll_no)
        print("Course    :", self.get_course())
class OnlineStudent(Student):
    def student_type(self):
        print("\nStudent Type : Online")
    def display(self):
        self.student_type()
        print("Name      :", self.name)
        print("Roll No   :", self.roll_no)
        print("Course    :", self.get_course())
s1 = RegularStudent("Priya", 22)
s2 = OnlineStudent("Vishnu", 8)
s1.display()
print("\nUpdating Course...")
s1.set_course("Data Science")
s1.display()
print()
s2.display()
