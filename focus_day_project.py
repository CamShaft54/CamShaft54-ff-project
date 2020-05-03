import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key
import random
import threading
import time

# Prompt user to enter Height and Width in pixels, radius of circles, and mass.
H = int(input("Enter Height of Gym: "))
W = int(input("Enter Width of Gym: "))
radius = int(input("Enter Radius of Ball: "))
mass = 1
bounce = 0
Bottom_Left_Corner = ((1280 - W) // 2, 600 - H)
Bottom_Right_Corner = ((1280 - W) // 2 + W, 600 - H)
Top_Left_Corner = ((1280 - W) // 2, 600)
Top_Right_Corner = ((1280 - W) // 2 + W, 600)
# Create Pyglet Window
window = pyglet.window.Window(1280, 720, "Pymunk Testing", resizable=False)
options = DrawOptions()
# Declare space to put bodies/shapes in
space = pymunk.Space()
space.gravity = 0, -1000
# Make gym base
segment_shape_base = pymunk.Segment(space.static_body, (0, 0), (W, 0), 5)
segment_shape_base.body.position = Bottom_Left_Corner
segment_shape_base.elasticity = bounce
segment_shape_base.friction = 1.0
# Make gym left wall
segment_shape_left = pymunk.Segment(space.static_body, (0, H), (0, 0), 5)
segment_shape_left.body.position = Bottom_Left_Corner
segment_shape_left.elasticity = bounce
segment_shape_left.friction = 1.0
# Make gym right wall
segment_body_right = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_body_right.position = Bottom_Right_Corner
segment_shape_right = pymunk.Segment(segment_body_right, (0, H), (0, 0), 5)
segment_shape_right.elasticity = bounce
segment_shape_right.friction = 1.0
# Make gym top wall
segment_body_top = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_body_top.position = Top_Left_Corner
segment_shape_top = pymunk.Segment(segment_body_top, (0, 0), (W, 0), 5)
segment_shape_top.elasticity = bounce
segment_shape_top.friction = 1.0
# Make left funnel
segment_body_left_fun = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_body_left_fun.position = 0, 0
segment_shape_left_fun = pymunk.Segment(segment_body_left_fun, (0, 720), Top_Left_Corner, 5)
segment_shape_left_fun.elasticity = bounce
segment_shape_left_fun.friction = 1.0
# Make right funnel
segment_body_right_fun = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_body_right_fun.position = 0, 0
segment_shape_right_fun = pymunk.Segment(segment_body_right_fun, (1280, 720), Top_Right_Corner, 5)
segment_shape_right_fun.elasticity = bounce
segment_shape_right_fun.friction = 1.0
# add gym walls to and funnel walls to wall shapes so they won't get counted multiple times or deleted.
wall_shapes = [segment_shape_base, segment_shape_left, segment_shape_right, segment_shape_top, segment_shape_right_fun
               , segment_shape_left_fun, segment_body_top, segment_shape_top]
checked_shapes = []
new_balls = []
previous_new_balls = []
tests = []
# Add gym walls and funnel walls to space
space.add(segment_shape_base, segment_shape_left, segment_shape_right, segment_body_right, segment_shape_left_fun
          , segment_body_left_fun, segment_shape_right_fun, segment_body_right_fun)
ball_spawning = False
auto = False
timer = 0


def make_ball(x, y):  # Makes ball from given coordinates and adds it to space
    circle_moment = pymunk.moment_for_circle(mass, 0, radius)
    circle_body = pymunk.Body(mass, circle_moment)
    circle_body.position = x, y
    circle_shape = pymunk.Circle(circle_body, radius)
    circle_shape.elasticity = bounce
    circle_shape.friction = 1.0
    space.add(circle_body, circle_shape)


def random_ball(status):  # Generate a random ball between the specified coordinates
    if status:
        make_ball(random.randint((1280 - W) / 2, (1280 - W) / 2 + W), 650)


def auto_mode_disable():
    space.add(segment_shape_top, segment_body_top)
    event = threading.Event()
    event.wait(0.5)
    space.remove(segment_shape_top, segment_body_top)
    event.wait(1)
    space.add(segment_shape_top, segment_body_top)


@window.event  # draw the space in window
def on_draw():
    window.clear()
    space.debug_draw(options)


@window.event
def on_mouse_press(x, y, button, modifiers):  # When the mouse is clicked, add a new shape to space at mouse coords.
    make_ball(x, y)


@window.event
def on_key_press(symbol, modifiers):
    global ball_spawning, auto, new_balls
    if symbol == key.T and segment_shape_top not in space.shapes:
        space.add(segment_shape_top, segment_body_top)
    elif symbol == key.T and segment_shape_top in space.shapes:
        space.remove(segment_shape_top.body, segment_shape_top)
    if symbol == key.B:
        ball_spawning = not ball_spawning
    if symbol == key.C:
        for shape in space.shapes:
            if shape not in wall_shapes:
                space.remove(shape.body, shape)
        checked_shapes.clear()
    if symbol == key.A:
        print("Auto mode enabled")
        ball_spawning = not ball_spawning
        auto = True
    if symbol == key.D:
        for shape in space.shapes:
            if shape.body.position.y >= 600 and shape not in wall_shapes:
                space.remove(shape.body, shape)
                new_balls.remove(shape)


def update(dt):  # Increase physics simulation by one, check if object's position is y <= 470, if so add it to
    # checked shapes, print checked shapes amount if different.
    global checked_shapes, ball_spawning, auto, new_balls, previous_new_balls, timer
    space.step(dt)
    changed_list = False
    previous_new_balls = new_balls
    for shape in space.shapes:
        if shape.body.position.y <= 600 - radius and shape not in checked_shapes and shape not in wall_shapes:
            checked_shapes.append(shape)
            changed_list = True
        if shape.body.position.y > 600 - radius and shape not in wall_shapes and timer == 0:
            new_balls.append(shape)
        if shape.body.position.y < 600 and shape in new_balls:
            new_balls.remove(shape)
        if shape.body.position.y < (600 - H) and shape not in wall_shapes:
            if shape in checked_shapes:
                checked_shapes.remove(shape)
            space.remove(shape.body, shape)
            changed_list = True
    random_ball(ball_spawning)
    if changed_list:
        print(str(len(checked_shapes)) + " balls")
    timer = (timer + 1) % 120
    execute = True
    if timer == 0 and auto:
        print("checking for overflow...")
        for i in range(min(len(previous_new_balls), len(new_balls))):
            if previous_new_balls[i].body.position == new_balls[i].body.position:
                if execute:
                    ball_spawning = False
                    auto = False
                    new_balls.clear()
                    auto_mode_disable()
                    for shape in space.shapes:
                        if shape.body.position.y >= 600 and shape not in wall_shapes:
                            space.remove(shape.body, shape)
                    tests.append(len(checked_shapes))
                    checked_shapes.clear()
                    print("Auto mode disabled")
                    print("Test results: " + str(tests))
                break


if __name__ == "__main__":  # Driver code to update simulation
    pyglet.clock.schedule_interval(update, 1.0 / 60)
    pyglet.app.run()