from math import pi


class Figure:
    def __init__(self, side):
        self._side = side
        self._area = None

    def __eq__(self, other):
        return self.area == other.area

    def __gt__(self, other):
        return self.area > other.area

    def __lt__(self, other):
        return self.area < other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __le__(self, other):
        return self.area <= other.area

    @property
    def side(self):
        return self._side

    @property
    def area(self):
        return self._area


class Circle(Figure):
    def __init__(self, side=1):
        super().__init__(side)

        self._diameter = 2 * self.side
        self._area = pi * self.side ** 2

    def __repr__(self):
        return f"Circle ({self.side})"



    def __add__(self, other):
        if self.__class__ == other.__class__:
            return self.area + other.area
        else:
            new_area = self.area + other.area
            new_radius = (new_area / pi) ** (1 / 2)
            return Circle(new_radius)

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
            self._diameter = 2 * value
            self._area = pi * self._side ** 2
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value > 0:
            self._area = value
            self._side = (self._area / pi) ** (1 / 2)
            self._diameter = self.side * 2
        else:
            raise ValueError("Area cannot be negative")

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if value > 0:
            self._diameter = value
            self._side = value / 2
            self._area = pi * self._side ** 2
        else:
            raise ValueError("Diameter cannot be negative")


class Square(Figure):
    def __init__(self, side):
        super().__init__(side)

        self._area = side ** 2

    def __repr__(self):
        return f"Square ({self.side})"

    def __add__(self, other):
        if self.__class__ == other.__class__:
            return self.area + other.area
        else:
            new_area = self.area + other.area
            new_side = new_area ** (1 / 2)
            return Square(new_side)

    @property
    def side(self):
        return self._side

    @property
    def area(self):
        return self._area

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
            self._area = value ** 2
        else:
            raise ValueError("Side cannot be negative")

    @area.setter
    def area(self, value):
        if value > 0:
            self._area = value
            self._side = value ** (1 / 2)
        else:
            raise ValueError("Area cannot be negative")


class Triangle(Figure):
    def __init__(self, side):
        super().__init__(side)

        self._area = side ** 2 / 2

    def __repr__(self):
        return f"Triangle ({self.side})"

    def __add__(self, other):
        if self.__class__ == other.__class__:
            return self.area + other.area
        else:
            new_area = self.area + other.area
            new_side = (new_area * 2) ** (1 / 2)
            return Triangle(new_side)


    @property
    def side(self):
        return self._side

    @property
    def area(self):
        return self._area

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
            self._area = value ** 2 / 2
        else:
            raise ValueError("Side cannot be negative")

    @area.setter
    def area(self, value):
        if value > 0:
            self._area = value
            self._side = (value * 2) ** (1 / 2)
        else:
            raise ValueError("Area cannot be negative")