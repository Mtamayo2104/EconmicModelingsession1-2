import random

class Point:
    def __init__(self, x, y):
        """
        initialize a point object
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        magic method that is called when we try to print an instance
        :return: <x, y>
        """
        return f"p({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()

    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5 # square root of the sum of x and y

    def __gt__(self, other):
        my_distance = self.distance_origin()
        other_distance = other.distance_origin()
        return my_distance > other_distance

    def __eq__(self, other):
        my_distance = self.distance_origin()
        other_distance = other.distance_origin()
        return my_distance == other_distance


if __name__ == "__main__":

    # now we need to initiate it:
    p = Point(1, 2)
    p2 = Point(2, 3)
    p4 = Point(4.4, -55)
    print(f"p.x= {p.x} and p.y={p.y}")
    print(f"p42.x= {p2.x} and p2.y={p2.y}")
    print(f"p4.x= {p4.x} and p4.y={p4.y}")
    p.x = 20
    print(f"p.x= {p.x} and p.y={p.y}")

    print(p)


    # the final purpose is to sort the list of final points

    p= Point(3,4)
    print(p.distance_origin())
    p2 = Point(1,1)
    print(f"im comparing p > p2: {p>p2}")

    # create a list of 5 random points
    points = []
    for i in range (5):
        points.append(Point(random.randint(-10, 10),random.randint(-10,10)))

    print("I got these 5 random points:")
    for p in points:
        print(p)

    print("the sorted list of points:")
    points.sort()
    print(points)
