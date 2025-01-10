import math

class Shape:
    def calculate_area(self):
        print("Calling wrong method for base class.")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

def display_area(shape):
    print(f"The area is: {shape.calculate_area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

display_area(circle)
display_area(rectangle)
display_area(triangle)
