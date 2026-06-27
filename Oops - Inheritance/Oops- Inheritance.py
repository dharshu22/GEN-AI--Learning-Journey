print("--------------Single Inheritance---------------")
class Person:
    def display_name(self):
        print("Name: Priya")
class Student(Person):
    def display_course(self):
        print("Course: Python")
s = Student()
s.display_name()
s.display_course()
print('-'*30)


print("-------------Mulitple Inheritance--------------")
class Student:
    def student_info(self):
        print("Name: Priya")
class Course:
    def course_info(self):
        print("Course: Python")
class Result(Student, Course):
    def display(self):
        print("Result: Pass")
r = Result()
r.student_info()
r.course_info()
r.display()
print('-'*30)

print("--------------Hybrid Inheritance---------------")
class Person:
    def person_info(self):
        print("Name: Priya")
class Student(Person):
    def student_info(self):
        print("Course: Python")
class Teacher(Person):
    def teacher_info(self):
        print("Subject: Programming")
class Result(Student, Teacher):
    def result(self):
        print("Result: Pass")
r = Result()
r.person_info()
r.student_info()
r.teacher_info()
r.result()
