class Square:
    def __init__(self, side):
        self._side = side
        self._area = side ** 2

    def __repr__(self):
        return f"Square ({self.side})"

    def __eq__(self, other):
        return self.side == other.side

    def __gt__(self, other):
        return self.side > other.side

    def __lt__(self, other):
        return self.side < other.side

    def __ge__(self, other):
        return self.side >= other.side

    def __le__(self, other):
        return self.side <= other.side

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
