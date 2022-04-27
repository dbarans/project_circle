import math
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2*radius
        self.area = pi*radius**2
