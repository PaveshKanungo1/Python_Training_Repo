print("Program to calculate the Area and Perimeter of Square, Rectangle, Parallelogram, Triangle, Circle")

print("\n")

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")    
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

print("\"Program to calculate the Area and Perimeter of Square\"")
side = get_valid_input("Enter the side of the square: ")
area = side * side
perimeter = 4 * side
print("Area of the square is: ", area)
print("Perimeter of the square is: ", perimeter)

print("\n")

print("\"Program to calculate the Area and Perimeter of Rectangle\"")
length = get_valid_input("Enter the length of the rectangle: ")
breadth = get_valid_input("Enter the breadth of the rectangle: ")
area = length * breadth
perimeter = 2 * (length + breadth)
print("Area of the rectangle is: ", area)
print("Perimeter of the rectangle is: ", perimeter)

print("\n")

print("\"Program to calculate the Area and Perimeter of Parallelogram\"")
base = get_valid_input("Enter the base of the parallelogram: ")
height = get_valid_input("Enter the height of the parallelogram: ")
area = base * height
perimeter = 2 * (base + height)
print("Area of the parallelogram is: ", area)
print("Perimeter of the parallelogram is: ", perimeter)

print("\n")

print("\"Program to calculate the Area and Perimeter of Triangle\"")
base = get_valid_input("Enter the base of the triangle: ")
height = get_valid_input("Enter the height of the triangle: ")
area = 0.5 * base * height
perimeter = 3 * base
print("Area of the triangle is: ", area)
print("Perimeter of the triangle is: ", perimeter)

print("\n")

print("\"Program to calculate the Area and Perimeter of Circle\"")
radius = get_valid_input("Enter the radius of the circle: ")
area = 3.14 * radius * radius
perimeter = 2 * 3.14 * radius
print("Area of the circle is: ", area)
print("Perimeter of the circle is: ", perimeter)

print("\n")

print("End of the program")
