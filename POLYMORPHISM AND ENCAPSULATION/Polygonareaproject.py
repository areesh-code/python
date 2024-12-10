class Polygon:
    def __init__(self):
        pass
    def area(self):
         
        raise NotImplementedError("Subclass must implement this method.")

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        return 0.5 * self.base * self.height

import math
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":

     rectangle = Rectangle(5, 10)
square = Square(4)
triangle = Triangle(6, 8)
circle = Circle(7)

print(f"Area of Rectangle: {rectangle.area()} square units")
print(f"Area of Square: {square.area()} square units")
print(f"Area of Triangle: {triangle.area()} square units")
print(f"Area of Circle: {circle.area():.2f} square units")


