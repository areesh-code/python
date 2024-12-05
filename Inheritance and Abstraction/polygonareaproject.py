class Polygon:
    def __init__(self, *sides):
        self.sides = sides
    def area(self):
        raise NotImplementedError("This method should be implemented by subclasses.")
    def perimeter(self):
        return sum(self.sides)
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    def area(self):
        return self.length * self.length
    
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(base, height)
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

import math

class Circle(Polygon):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
if __name__ == "__main__":
     rect = Rectangle(5, 3)
square = Square(4)
triangle = Triangle(4, 6)
circle = Circle(7)

print(f"Rectangle area: {rect.area()} square units")
print(f"Rectangle perimeter: {rect.perimeter()} units")
    
print(f"Square area: {square.area()} square units")
print(f"Square perimeter: {square.perimeter()} units")
    
print(f"Triangle area: {triangle.area()} square units")
print(f"Triangle perimeter: {triangle.perimeter()} units")
    
print(f"Circle area: {circle.area():.2f} square units")
print(f"Circle perimeter (circumference): {circle.perimeter():.2f} units")







