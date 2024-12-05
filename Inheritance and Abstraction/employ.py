class Person:
    def __init__(self, name, idnumber):
        self.name= name
        self.idnumber = idnumber
    def present(self):
        print(self.name, self.idnumber)

class Employee(Person): 
    def __init__(self, name, idnumber, salary, age):
        self.salary = salary
        self.age = age
        Person.__init__(self, name, idnumber)

obj = Employee("Areesh", 6923145, 2300, 27)
obj.present()
    
