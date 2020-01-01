import turtle

FILENAME: str = "./src/turtle_commands_inoneline.txt"


def main():
    t = turtle.Turtle()
    screen = t.getscreen()

    with open(file=FILENAME, mode="r") as f:
        for line in f:
            text = line.strip()
            command_list = text.split(",")
            command = command_list[0]

            if command == "goto":
                x, y = float(command_list[1]), float(command_list[1])
                width = float(command_list[3])
                color = command_list[4].strip()
                t.width(width=width)
                t.pencolor(color)
                t.goto(x, y)

            elif command == "circle":
                radius, width = float(command_list[1]), float(command_list[2])
                color = command_list[3].strip()
                t.width(width=width)
                t.pencolor(color)
                t.circle(radius=radius)

            elif command == "beginfill":
                color = command_list[1].strip()
                t.fillcolor(color)
                t.begin_fill()

            elif command == "endfill":
                t.end_fill()

            elif command == "penup":
                t.penup()

            elif command == "pendown":
                t.pendown()

            else:
                print(f"Unknown command found in file: {command}")

        t.hideturtle()

        screen.exitonclick()
        print("Program Execution Completed.")

if __name__ == "__main__":
    main()
