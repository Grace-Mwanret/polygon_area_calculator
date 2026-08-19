import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, square):
        return self.width // square.width * self.height // square.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_width(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_height(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def __str__(self):
        return f"Square(side={self.width})"




