# About

This project is a Python program that demonstrates object-oriented programming (OOP) by creating Rectangle and Square classes.
The Square class inherits functionality from the Rectangle class and uses super() to initialize its width and height

# What It Does

The program allows you to:

Create rectangles and squares.
Set and change their width and height.
Calculate the area.
Calculate the perimeter.
Calculate the diagonal.
Generate a picture of the shape using *.
Determine how many times one shape can fit inside another.
Display information about the shapes using __str__().

# How to Run It
1. Make sure Python is installed. You can check by running: python --version
2. Save the code. Save the program as a Python file, for example: shapes.py
3. Open your terminal in the project folder Run: python shapes.py
The program will print the calculated areas, perimeters, diagonals, shape information, and pictures.

# What I Learned

Through this project, I learned how to:

1. Create classes and objects in Python.
2. Use the __init__() constructor.
3. Create and modify object attributes.
4. Create methods inside a class.
5. Use inheritance with class Square(Rectangle).
6. Use super() to call the parent class's constructor.
7. Override the __str__() method.
8. Use math.sqrt() to calculate a diagonal.
9. Use string multiplication to create a shape using *.
10. Use integer division (//) to determine how many shapes can fit inside another shape.
11. Reuse methods from a parent class instead of rewriting them.

# Example input
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

# Example output
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
