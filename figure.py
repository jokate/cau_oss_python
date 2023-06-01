import math

class line:
    __height = 0
    __width = 0
    def __init__(self, width, height):
        self.__height = height
        self.__width = width

    def set_length(self, width, height):
        self.__height = height
        self.__width = width

    def get_length(self):
        return self.__height, self.__width

def area_rectangle(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height


def area_ellipse(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi


def area_right_triangle(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2