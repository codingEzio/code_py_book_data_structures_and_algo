from __future__ import annotations
import turtle


class Point(turtle.RawTurtle):
    """This class was merely used for demonstrating the sorting mechanism.
    """

    def __init__(self, canvas, x, y):
        super().__init__(canvas)
        canvas.register_shape(
            "dot",
            (
                (3, 0),
                (2, 2),
                (0, 3),
                (-2, 2),
                (-3, 0),
                (-2, -2),
                (0, -3),
                (2, -2),
            ),
        )
        self.shape("dot")
        self.speed(0)  # fastest
        self.penup()
        self.goto(x, y)

    def __str__(self):
        return f"({str(self.xcor()), str(self.ycor())})"

    # There's some exceptions among lexicographical ordering sequences,
    # ~ NAH    [1, 2] < ['a', 'b']
    # ~ OKAY   [1, 2, 'b'] < [1, 3, 'c']
    def __lt__(self, other: Point):
        return self.ycor() < other.ycor()


def main() -> None:
    t = turtle.Turtle()
    t.hideturtle()
    screen = t.getscreen()
    list_of_points = []

    i: int
    j: int
    for i in range(3):
        for j in range(3):
            pair = Point(screen, i, j)
            list_of_points.append(pair)
    list_of_points.sort()

    # The only result we care about, i.e. ordered points
    for point in list_of_points:
        print(point)


if "__main__" == __name__:
    main()
