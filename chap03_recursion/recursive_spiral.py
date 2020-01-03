import turtle


def draw_spiral(t: turtle.Turtle, length: int, color: str, color_base: str):
    if length == 0:
        return None

    new_color = (int(color[1:], 16) + 2 ** 10) % (2 ** 24)
    base = int(color_base[1:], 16)

    if new_color < base:
        new_color = (new_color + base) % (2 ** 24)

    new_color = hex(new_color)[2:]
    new_color = "#" + \
                "0" * (6 - len(new_color)) + \
                new_color

    t.color(new_color)
    t.forward(length)
    t.left(90)

    # Note it's the `minus 1` make the program towards the end.
    draw_spiral(t=t, length=length - 1, color=new_color, color_base=color_base)


def main():
    t = turtle.Turtle()
    screen = t.getscreen()

    t.speed(0)  # 0~10 fastest -> slowest
    t.penup()
    t.goto(-100, -100)
    t.pendown()

    draw_spiral(t=t, length=150, color="#ffffff", color_base="#ff0000")


if __name__ == "__main__":
    main()
