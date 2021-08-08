# source: Advanced Guide to Python 3 Programming p24
import turtle

WIDTH = 640
HEIGHT = 360


def setup_window():
    # Set up the window
    turtle.title('Circles in my mind')
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    turtle.colormode(255)
    turtle.hideturtle()
    # batch drawing to the screen for faster rendering
    turtle.tracer(2000)
    turtle.speed(10)
    turtle.penup()


def draw_circle(x, y, radius, red=50, green=255, blue=10, width=7):
    """'Draw a circle with specific x y location.'"""
    colour=(red, green, blue)

    # recursively draw smaller circle
    if radius > 50:
        # calculate colours and line width for smaller circles
        if red < 216:
            red += 33
            green -= 42
            blue += 10
            width -= 1
        else:
            red = 0
            green = 255

        new_radius = int(radius/1.3)
        # draw four circles
        draw_circle(int(x + new_radius), y, new_radius, red, green, blue, width)
        draw_circle(int(x - new_radius), y, new_radius, red, green, blue, width)
        draw_circle(x, int(y + new_radius), new_radius, red, green, blue, width)
        draw_circle(x, int(y - new_radius), new_radius, red, green, blue, width)

    turtle.goto(x, y)
    turtle.color(colour)
    turtle.width(width)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

# run the program
print('....STARTING....')
setup_window()
draw_circle(25, -100, 200)

# update and rendered
turtle.update()
print('......DONE..........')
turtle.done()
