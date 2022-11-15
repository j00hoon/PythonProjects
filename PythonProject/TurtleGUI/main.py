from turtle import Turtle, Screen
import matplotlib.pyplot as plt
import random
import colorgram


screen = Screen()
turtle = Turtle()
turtle.shape("classic")
turtle.color("green")



# for _ in range(35):
#     turtle.forward(5)
#     turtle.penup()
#     turtle.forward(5)
#     turtle.pendown()


# plt.hlines(y=1, xmin=0, xmax=10, color='pink', linestyle='dashed')
# plt.show()


#colors = ["IndianRed","DarkOrchid","CornflowerBlue","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
angles = ["right", "left"]
directions = ["back", "forward"]
distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tilts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
pen_size = [5, 10, 15, 20, 25]
pen_speed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def draw_shapes(angle, count):
#     for _ in range(count):
#         turtle.forward(100)
#         turtle.right(angle)
#
# for num_sides in range(3, 10):
#     turtle.color(colors[random.randrange(0, len(colors))])
#     angle = 360 / num_sides
#     draw_shapes(angle, num_sides)



def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    color = (r, g, b)
    return color



def draw_random(count):
    screen.colormode(255)
    for _ in range(count):
        turtle.color(random_color())
        dist = distance[random.randrange(0, len(distance))]
        tilt = tilts[random.randrange(0, len(tilts))]
        turtle.pensize(pen_size[random.randrange(0, len(pen_size))])
        turtle.speed(pen_speed[random.randrange(0, len(pen_speed))])

        if random.randrange(0, len(angles)) == 0:
            turtle.right(tilt)
        else:
            turtle.left(tilt)
        if random.randrange(0, len(directions)) == 0:
            turtle.back(dist)
        else:
            turtle.forward(dist)



def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        screen.colormode(255)
        turtle.speed("fastest")
        turtle.circle(50)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + size_of_gap)
        turtle.color(random_color())


def extract_colors():
    rgb_colors = []
    colors = colorgram.extract("spot.jpg", 30)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)


def draw_spot(color_list):
    x_pos = 0
    y_pos = 0

    for y in range(10):
        turtle.penup()
        turtle.setpos(x_pos, y_pos)
        turtle.pendown()
        for x in range(10):
            turtle.pendown()
            screen.colormode(255)
            turtle.dot(20, random.choice(color_list))
            turtle.penup()
            turtle.forward(50)
        x_pos = 0
        y_pos += 25

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.right(180)
    turtle.forward(10)

def turn_left():
    turtle.left(10)
    #new_heading = turtle.heading() + 10
    #turtle.setheading(new_heading)

def turn_right():
    turtle.right(10)
    # new_heading = turtle.heading() - 10
    # turtle.setheading(new_heading)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def draw_etch_a_sketch():
    screen.listen()
    screen.onkeypress(move_forwards, "w")
    screen.onkeypress(turn_left, "a")
    screen.onkeypress(turn_right, "d")
    #screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    # screen.onkey(turn_left, "a")
    # screen.onkey(turn_right, "d")
    screen.onkey(clear_screen, "c")


color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

#draw_random(30)
#draw_circle(10)
#extract_colors()

#draw_spot(color_list)

draw_etch_a_sketch()



screen.exitonclick()



