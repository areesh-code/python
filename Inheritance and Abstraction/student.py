class Person:
    def __init__(self, name, yearborn, age):
        self.name = name
        self.yearborn = yearborn
        self.age = age
    def display(self):
        print(self.name, self.yearborn, self.age)

class Student(Person):
    def __init__(self, name, yearborn, roomnumber):
        super().__init__(name, yearborn)
        self.roomnumber = roomnumber
        

obj = Student ("Areesh", 2011, 13, 24)
obj.display()
print(obj.age, obj.roomnumber)
