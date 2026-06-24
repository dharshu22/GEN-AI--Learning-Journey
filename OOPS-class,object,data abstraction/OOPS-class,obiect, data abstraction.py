print("OBJECT ORIENTED PROGRAMMING STRUCTURE")
print("Person Details Using Class and Object")
class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display(self):
        print("Name:", self.name)
        print("City:", self.city)

p1 = Person("Priya", "Chennai")
p1.display()
print('*'*30)

print("Payment Method in Data Abstraction:")
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Payment Completed")
p = UPI()
p.pay()
print('*'*30)

print("Login System in Data Abstraction:")
from abc import ABC, abstractmethod
class Login(ABC):
    @abstractmethod
    def authenticate(self):
        pass
class User(Login):
    def authenticate(self):
        print("Login Successful")
u = User()
u.authenticate()



