import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key

# Create Pyglet Window
window = pyglet.window.Window(1280, 720, "Pymunk Testing", resizable=False)
options = DrawOptions()
# Declare space to put bodies/shapes in
space = pymunk.Space()
space.gravity = 0, -1000
# Set mass and radius of circle
mass = 1
radius = 30
# Make gym base
segment_shape_base = pymunk.Segment(space.static_body, (0, 0), (800, 0), 2)
segment_shape_base.body.position = 200, 70
segment_shape_base.elasticity = 0
segment_shape_base.friction = 1.0
# Make gym left wall
segment_shape_left = pymunk.Segment(space.static_body, (0, 500), (0, 0), 2)
segment_shape_left.body.position = 200, 70
segment_shape_left.elasticity = 0
segment_shape_left.friction = 1.0
# Make gym right wall
segment_body_right = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_body_right.position = 1000, 70
segment_shape_right = pymunk.Segment(segment_body_right, (0, 500), (0, 0), 2)
segment_shape_right.elasticity = 0
segment_shape_right.friction = 1.0
# Make gym top wall
segment_body_top = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_body_top.position = 200, 570
segment_shape_top = pymunk.Segment(segment_body_top, (0, 0), (800, 0), 2)
segment_shape_top.elasticity = 0
segment_shape_top.friction = 1.0
# add gym walls to checked shapes so they won't get counted multiple times.
checked_shapes = [segment_shape_base, segment_shape_left, segment_shape_right, segment_shape_top]
# Add gym base, right, left walls to space
space.add(segment_shape_base, segment_shape_left, segment_shape_right, segment_body_right)


@window.event  # draw the space when window opens
def on_draw():
    window.clear()
    space.debug_draw(options)


@window.event
def on_mouse_press(x, y, button, modifiers):  # When the mouse is clicked, add a new shape to space
    circle_moment = pymunk.moment_for_circle(mass, 0, radius)
    circle_body = pymunk.Body(mass, circle_moment)
    circle_body.position = x, y
    circle_shape = pymunk.Circle(circle_body, radius)
    circle_shape.elasticity = 0
    circle_shape.friction = 1.0
    space.add(circle_body, circle_shape)


@window.event
def on_key_press(symbol, modifiers):  # When T is pressed add top segment, if top segment is already there, remove it.
    if symbol == key.T and segment_shape_top not in space.shapes:
        print("Top segment added")
        space.add(segment_shape_top, segment_body_top)
    elif symbol == key.T and segment_shape_top in space.shapes:
        space.remove(segment_shape_top.body, segment_shape_top)


def update(dt):  # Increase physics simulation by one, check if object's position is y <= 470, if so add it to
    # checked shapes, print checked shapes excluding walls.
    global checked_shapes
    space.step(dt)
    for shape in space.shapes:
        if shape.body.position.y <= 470 and shape not in checked_shapes:
            checked_shapes.append(shape)
    print(len(checked_shapes)-3)


if __name__ == "__main__":  # Driver code to update simulation
    pyglet.clock.schedule_interval(update, 1.0 / 60)
    pyglet.app.run()
