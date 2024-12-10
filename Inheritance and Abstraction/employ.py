class Person:
    def __init__(self, name, idnumber, age):
        self.name= name
        self.idnumber = idnumber
        self.age = age
    def present(self):
        print(self.name, self.idnumber, self.age)

class Employee(Person): 
    def __init__(self, name, idnumber, age, salary, roomnumber):
        self.salary = salary
        self.roomnumber= roomnumber
        
        Person.__init__(self, name, idnumber, age)

obj = Employee("Areesh", 353545, 2300, 27, 69)
obj.present()
    
