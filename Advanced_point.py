from color_point import Colorpoint


class Pointexception(Exception):
    pass


class AdvancedPoint (Colorpoint):
    COLORS = ["red","blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        """
        Validates the color against the class's predefined COLORS list and raises an exception
        for invalid colors. Initializes the instance with the provided coordinates and color.

        Args:
            x (int | float): The x-coordinate of the point.
            y (int | float): The y-coordinate of the point.
            color (str): The color name for the point. Must be a value from the class's COLORS list.

        Raises:
            Pointexception: If the specified color is not found in the class's COLORS list.
        """
        if color not in self.COLORS:
            raise Pointexception(f"invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        gets the x coordinate

        """
        return self._x# getter method

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the point.
        """
        self._x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the point.

        """
        return self._y

    @property
    def color(self):
        """
        gets the color of the point
        """
        return self._color

    @classmethod  # class methods applies to the whole class, no individual objects
    def add_color(cls, color):
        """
        adds a new valid color for our class
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        creates anew point from a tuple rather than 2 individual values
        """
        x, y = coordinate
        return AdvancedPoint(x,y,color)
    @staticmethod
    def distance_2_points(p1,p2):
        """
        measure distances between 2 points
        :param p1: point 1
        :param p2: point 2
        :return: distance between them
        """
        return ((p1.x - p2.x)**2 +(p1.y - p2.y)**2)**0.5

    def distance_other (self, p):
        """
        Computes the straight-line distance between this point (self) and another point (p)
        using the Pythagorean theorem.
        """
        return ((self.x - p.x)**2 +(self.y - p.y)**2)**0.5


AdvancedPoint.add_color("rojo")

p= AdvancedPoint(1,2,"blue")

print(p.x)
print(p)
print(p.distance_origin())
p2 = AdvancedPoint.from_tuple((3,2))
print(p2)

print(AdvancedPoint.distance_2_points(p,p2))
print(p.distance_other(p2))