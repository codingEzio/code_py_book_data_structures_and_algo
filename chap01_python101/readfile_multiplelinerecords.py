import turtle

FILENAME: str = "./src/turtle_commands_multiplelines.txt"


def main():
    t = turtle.Turtle()
    screen = t.getscreen()

    with open(file=FILENAME, mode="r") as file:
        command = file.readline().strip()

        while command != "":
            if command == "goto":
                x, y = float(file.readline()), float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                t.width(width=width)
                t.pencolor(color)
                t.goto(x, y)
            elif command == "circle":
                radius, width = float(file.readline()), float(file.readline())
                color = file.readline().strip()
                t.width(width=width)
                t.pencolor(color)
                t.circle(radius=radius)
            elif command == "beginfill":
                color = file.readline().strip()
                t.begin_fill()
            elif command == "endfill":
                t.end_fill()
            elif command == "penup":
                t.penup()
            elif command == "pendown":
                t.pendown()
            else:
                print(f"Unknown command found in file: {command}")

            command = file.readline().strip()

        t.hideturtle()
        screen.exitonclick()
        print("Program execution completed.")


if __name__ == "__main__":
    main()
