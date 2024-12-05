class Person:
    def __init__(self, name, yearborn):
        self.name = name
        self.yearborn = yearborn
    def display(self):
        print(self.name, self.yearborn)

class Student(Person):
    def __init__(self, name, yearborn, roomnumber, age):
        super().__init__(name, yearborn)
        self.roomnumber = roomnumber
        self.age = age

obj = Student ("Areesh", 2011, 24, 13)
obj.display()
print(obj.age, obj.roomnumber)
