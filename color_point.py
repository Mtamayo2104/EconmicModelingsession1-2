import random

from point import Point


class Colorpoint(Point):
    def __init__(self, x, y, color):
        # raise an exception if we try to have a not number
        if not isinstance(x, (int,float)):
            raise TypeError ("x must be a number")
        if not isinstance(y, (int,float)):
            raise TypeError ("y must be a number")

        super().__init__(x,y) # this replaces the self.x and slef.y
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x},{self.y}>"

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



