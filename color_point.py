import random

from point import Point


class Colorpoint(Point):
    def __init__(self, x, y, color):
        """
        Initializes a Point object with x and y coordinates and a color.

        Delegates the initialization of x and y coordinates to the parent class
        and sets the color attribute for this instance. Raises a TypeError if
        x or y is not a number.

        Args:
            x (int or float): The x-coordinate of the point.
            y (int or float): The y-coordinate of the point.
            color: The color associated with the point (no type restriction).

        Raises:
            TypeError: If x or y is not an integer or float.
        """
        # Raise an exception if we try to have a non-number
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        super().__init__(x, y)  # Delegate x, y initialization to parent class
        self.color = color

    def __str__(self):
        """
        Returns a human-readable string representation of the Point object.

        The string is formatted as '<color: x,y>', where color is the point's color,
        and x and y are the point's coordinates.

        Returns:
            str: A string describing the point in the format '<color: x,y>'.
        """
        return f"<{self.color}: {self.x},{self.y}>"


if __name__ == "__main__":
    p= Colorpoint(1,2,"Red")
    print(p.distance_origin())
    print(p)

# colors = ["red", "green", "blue", "yellow", "black", "magenta", "cyan"
#           , "white", "burgundy", "periwinkle", "marsala"]
#
# color_points = []
# for i in range(10):
#     color_points.append(
#         Colorpoint(random.randint(-10,10),
#                    random.randint(-10,10),
#                    random.choice(colors)))
#
#
# print(color_points)
# color_points.sort()
# print(color_points)



