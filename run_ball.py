import turtle
import ball
import random

def initilizing(canvas_width, canvas_height, ball_radius, xpos, ypos, vx, vy, color_list):
    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        xpos.append(random.randint(-1 * canvas_width + ball_radius,
                                        canvas_width - ball_radius))
        ypos.append(random.randint(-1 * canvas_height + ball_radius,
                                        canvas_height - ball_radius))
        vx.append(random.randint(1, 0.01 * canvas_width))
        vy.append(random.randint(1, 0.01 * canvas_height))
        color_list.append((random.randint(0, 255), random.randint(0, 255),
                                random.randint(0, 255)))


num_balls = int(input("Number of balls to simulate: "))
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
color_list = []
xpos = []
ypos = []
vx = []
vy = []

for i in range(num_balls):
    initilizing(canvas_width, canvas_height, ball_radius, xpos, ypos, vx, vy, color_list)
ball_type = ball.Ball(0.07 * canvas_width, turtle.speed(0), color_list, xpos, ypos, vx, vy )


while True:
    turtle.clear()
    for i in range(num_balls):
        ball.Ball.draw_circle(ball_type, i)
        ball.Ball.move_circle(ball_type, i, canvas_width, canvas_height)

    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()

