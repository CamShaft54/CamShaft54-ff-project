import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key
import random

# Prompt user to enter Height and Width in pixels, radius of circles, and define mass and bounce/elasticity.
H = int(input("Enter Height of Gym: "))
W = int(input("Enter Width of Gym: "))
radius = int(input("Enter Radius of Ball: "))
mass = 1
bounce = 0
# Given H and W of gym define coordinates of corners.
Bottom_Left_Corner = ((1280 - W) // 2, 600 - H)
Bottom_Right_Corner = ((1280 - W) // 2 + W, 600 - H)
Top_Left_Corner = ((1280 - W) // 2, 600)
Top_Right_Corner = ((1280 - W) // 2 + W, 600)
# Create Pyglet Window
window = pyglet.window.Window(1280, 720, "Pymunk Testing", resizable=False)
options = DrawOptions()
# Declare space to put bodies/shapes in, define gravity.
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
    , segment_shape_left_fun, segment_shape_top]
# define variables used later.
checked_shapes = []
new_balls = []
previous_new_balls = []
tests = []
ball_spawning = False
ball_cleanup = 0
auto = False
timer = 0
stop_time = 0
# Add gym walls and funnel walls to space.
space.add(segment_shape_base, segment_shape_left, segment_shape_right, segment_body_right, segment_shape_left_fun
          , segment_body_left_fun, segment_shape_right_fun, segment_body_right_fun)


def make_ball(x, y):  # Makes ball from given coordinates and adds it to space
    circle_moment = pymunk.moment_for_circle(mass, 0, radius)
    circle_body = pymunk.Body(mass, circle_moment)
    circle_body.position = x, y
    circle_shape = pymunk.Circle(circle_body, radius)
    circle_shape.elasticity = bounce
    circle_shape.friction = 1.0
    space.add(circle_body, circle_shape)


def random_ball(status):  # Generate a random ball between the specified coordinates.
    if status:
        make_ball(random.randint((1280 - W) / 2, (1280 - W) / 2 + W), 650)


@window.event  # draw the space in window
def on_draw():
    window.clear()
    space.debug_draw(options)


@window.event
def on_mouse_press(x, y, button, modifiers):  # When the mouse is clicked, add a new shape to space at mouse coords.
    make_ball(x, y)


@window.event
def on_key_press(symbol, modifiers):  # If a key is pressed...
    global ball_spawning, auto, new_balls
    if symbol == key.T and segment_shape_top not in space.shapes:  # If T, add the top wall if not already there.
        space.add(segment_shape_top, segment_body_top)
    elif symbol == key.T and segment_shape_top in space.shapes:  # If T, remove top wall if already there.
        space.remove(segment_shape_top.body, segment_shape_top)
    if symbol == key.B:  # If B, toggle ball_spawning variable (controls random_ball function called in update).
        ball_spawning = not ball_spawning
    if symbol == key.C:  # If C, clear all balls.
        for shape in space.shapes:
            if shape not in wall_shapes:
                space.remove(shape.body, shape)
        checked_shapes.clear()
    if symbol == key.A:  # If A, activate auto mode, remove top wall if there, toggle on ball_spawning.
        print("Auto mode enabled")
        if segment_shape_top in space.shapes:
            space.remove(segment_shape_top, segment_body_top)
        ball_spawning = not ball_spawning
        auto = True
    if symbol == key.D:  # If D, clear all balls above top wall.
        for shape in space.shapes:
            if shape.body.position.y >= 600 and shape not in wall_shapes:
                space.remove(shape.body, shape)
                new_balls.remove(shape)


def update(dt):  # This function is called every 1/60 of a second.
    global checked_shapes, ball_spawning, previous_new_balls, new_balls, auto, timer, ball_cleanup, stop_time
    space.step(dt)  # Step forward the physics simulation.
    changed_list = False  # Set changed_list to false (If true, print number of balls in checked_shapes).
    # If auto mode is active and 1 second has elapsed, check for overflow.
    if timer % 60 == 0 and auto and len(previous_new_balls) > 1:
        stop_time = timer
        print("checking for overflow...")
        # for loop checks balls from 2 seconds ago that are above top wall with current balls above top wall.
        for i in range(len(previous_new_balls)):
            # Check every ball from 2 seconds ago to see if still above.
            # Error: List index out of range
            print("i: " + str(i), "previous_balls: " + str(len(previous_new_balls)))
            current_previous_ball = (
            round(previous_new_balls[i].body.position.x), round(previous_new_balls[i].body.position.y))
            for j in range(len(new_balls)):
                print("j: " + str(j), "new_balls: " + str(len(new_balls)))
                current_new_ball = (round(new_balls[j].body.position.x), round(new_balls[j].body.position.y))
                print(current_previous_ball)
                print(current_new_ball)
                if abs(current_new_ball[0] - current_previous_ball[0]) < 50 and abs(
                        current_new_ball[1] - current_previous_ball[1]) < 50 and auto:
                    # If so, deactivate ball_spawning, deactivate auto mode, clear new_balls, clear previous_new_balls.
                    print("Auto mode turning off...")
                    ball_spawning = False
                    auto = False
                    new_balls.clear()
                    previous_new_balls.clear()
                    for shape in space.shapes:  # Remove all balls above top wall.
                        if shape.body.position.y >= 600 and shape not in wall_shapes:
                            space.remove(shape.body, shape)
                    space.add(segment_shape_top, segment_body_top)
                    ball_cleanup = 1  # Activate ball_cleanup.
                    break
            else:
                continue
            break
    timer = (timer + 1) % 120  # Progress timer forward by one.
    if timer == 1:  # Every two seconds (right after checking for overflow) set previous_new_balls equal to new_balls
        previous_new_balls = new_balls.copy()
    for shape in space.shapes:  # for loop checks all balls and adds or removes them from lists.
        # if ball in gym add to checked_shapes
        if shape.body.position.y <= 600 - radius and shape not in checked_shapes and shape not in wall_shapes:
            checked_shapes.append(shape)
            changed_list = True
        # If ball above gym height add to new_balls
        if shape.body.position.y > 600 - radius and shape not in new_balls and shape not in wall_shapes:
            new_balls.append(shape)
        # If ball in new_balls and below gym height, remove from new_balls
        if shape.body.position.y < 600 and shape in new_balls:
            new_balls.remove(shape)
        # If ball is below gym height remove from space and checked_shapes.
        if shape.body.position.y < (600 - H) and shape not in wall_shapes:
            if shape in checked_shapes:
                checked_shapes.remove(shape)
            space.remove(shape.body, shape)
            changed_list = True
    random_ball(ball_spawning)  # Spawn a random_ball if ball_spawning is True.
    if changed_list:  # If any balls were taken away or added to checked_shapes, print checked_shapes length.
        print(str(len(checked_shapes)) + " balls")
    if ball_cleanup == 1 and timer == stop_time + 29 % 120:  # after 0.5 seconds have passed since auto mode deactivation, remove top wall.
        space.remove(segment_shape_top, segment_body_top)
        ball_cleanup += 1
    if ball_cleanup == 2 and timer == stop_time + 119 % 120:  # after 2 seconds have passed, add back top wall, remove balls above wall, add current.
        space.add(segment_shape_top, segment_body_top)
        for shape in space.shapes:
            if shape.body.position.y >= 600 and shape not in wall_shapes:
                space.remove(shape.body, shape)
        print("Auto mode disabled")
        tests.append(len(checked_shapes))
        checked_shapes.clear()
        print("Test results: " + str(tests))
        ball_cleanup = 0


if __name__ == "__main__":  # Driver code to update simulation
    pyglet.clock.schedule_interval(update, 1.0 / 60)
    pyglet.app.run()
