print("------------Polymorphism--------------")
#Bank Account Program- Overriding Method (Polymorphism):
class SavingsAccount:
    def interest(self):
        print("Savings Account Interest: 5%")
class CurrentAccount:
    def interest(self):
        print("Current Account Interest: 0%")
accounts = [SavingsAccount(), CurrentAccount()]
for account in accounts:
    account.interest()
print('-'*30)

#Student and Teacher Details:
class Student:
    def details(self):
        print("Student: Priya")
class Teacher:
    def details(self):
        print("Teacher: Anitha")

people = [Student(), Teacher()]
for person in people:
    person.details()
print('-'*30)

#Exam Result Program:
class Result:
    def grade(self):
        print("Grade is calculated.")
class SchoolResult(Result):
    def grade(self):
        print("School Grade: A")
class CollegeResult(Result):
    def grade(self):
        print("College Grade: O")

school = SchoolResult()
college = CollegeResult()

school.grade()
college.grade()
print('-'*30)

