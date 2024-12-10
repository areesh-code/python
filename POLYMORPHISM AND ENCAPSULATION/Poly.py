class Student:
    def __init__(self, Room, Name, Class):
        self.Room = Room
        self.Name = Name
        self.Class = Class

    def Slideshow(self):
        print(self.Room)
        print(self.Name)
        print(self.Class)
    
class Sportman:
    def __init__(self, Room, Name, Class):
        self.Room= Room
        self.Name= Name
        self.Class= Class
    
    def Slideshow(self):
        print(self.Room, self.Name, self.Class)
    
obj1 = Student(24, "Areesh", 24)
obj2 = Sportman(31, "Jack", 31)

for i in (obj1, obj2):
    i.Slideshow()
        
    
        


        
