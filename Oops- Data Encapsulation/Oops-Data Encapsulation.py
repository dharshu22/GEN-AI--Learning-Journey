#Data Encapsulation-Mobile Phone:
class Mobile:
    def __init__(self, brand):
        self.__brand = brand
    def set_brand(self, brand):
        self.__brand = brand
    def get_brand(self):
        return self.__brand
phone = Mobile("OnePlus")
print("Brand:", phone.get_brand())
phone.set_brand("Nothing")
print("Updated Brand:", phone.get_brand())
print('*'*30)

#Area of Circle:
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def set_radius(self, radius):
        self.__radius = radius
    def get_area(self):
        return 3.14 * self.__radius * self.__radius
c = Circle(5)
print("Area:", c.get_area())
c.set_radius(7)
print("Updated Area:", c.get_area())
print('*'*30)

#Student details:
class Student:
    def __init__(self, name, marks):
        self.__name = name      
        self.__marks = marks
    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)
    def set_marks(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
s = Student("Priya", 90)
s.display()
s.set_marks(95)
print("Updated Marks:", s.get_marks())

