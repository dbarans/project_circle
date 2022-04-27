from math import pi


class Circle:
    def __init__(self, radius=1):
        self._radius = radius
        self._diameter = 2 * self._radius
        self._area = pi * self._radius ** 2

    def __repr__(self):
        return f"Circle ({self._radius})"

    def __eq__(self, other):
        return self._radius == other._radius

    def __gt__(self, other):
        return self._radius > other._radius

    def __lt__(self, other):
        return self._radius < other._radius

    def __ge__(self, other):
        return self._radius >= other._radius

    def __le__(self, other):
        return self._radius <= other._radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
            self._diameter = 2 * value
            self._area = pi * self._radius ** 2
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value > 0:
            self._area = value
            self._radius = (self._area / pi) ** (1 / 2)
            self._diameter = self.radius * 2
        else:
            raise ValueError("Area cannot be negative")

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if value > 0:
            self._diameter = value
            self._radius = value / 2
            self._area = pi * self._radius ** 2
        else:
            raise ValueError("Diameter cannot be negative")
