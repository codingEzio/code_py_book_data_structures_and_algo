import turtle
from turtlecommands import (
    GoToCommand,
    CircleCommand,
    BeginFillCommand,
    EndFillCommand,
    PenUpCommand,
    PenDownCommand,
)


class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def __iter__(self):
        for item in self.items:
            yield item


def main():
    filename = "./src/turtle_commands_multiplelines.txt"
    t = turtle.Turtle()
    screen = t.getscreen()
    graphic_commands = PyList()

    with open(file=filename, mode="r") as file:
        command = file.readline().strip()

        while command != "":
            if command == "goto":
                x, y = float(file.readline()), float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                cmd = GoToCommand(x, y, width, color)

            elif command == "circle":
                radius, width = float(file.readline()), float(file.readline())
                color = file.readline().strip()
                cmd = CircleCommand(radius, width, color)

            elif command == "beginfill":
                color = file.readline().strip()
                cmd = BeginFillCommand(color)

            elif command == "endfill":
                cmd = EndFillCommand()

            elif command == "penup":
                cmd = PenUpCommand()

            elif command == "pendown":
                cmd = PenDownCommand()

            else:
                raise RuntimeError(f"Unknown command: {command}")

            graphic_commands.append(cmd)
            command = file.readline().strip()

        for cmd in graphic_commands:
            cmd.draw(t)

        t.hideturtle()
        screen.exitonclick()

        print("Program execution completed.")


if __name__ == "__main__":
    main()
