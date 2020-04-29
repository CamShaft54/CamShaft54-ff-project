import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
# Create Pyglet Window
window = pyglet.window.Window(1280, 720, "Pymunk Testing", resizable=False)
options = DrawOptions()
# Declare space to put bodies/shapes in
space = pymunk.Space()
space.gravity = 0, -1000
# Set mass and radius of circle
mass = 1
radius = 30
# Make circle
circle_moment = pymunk.moment_for_circle(mass, 0, radius)
circle_body = pymunk.Body(mass, circle_moment)
circle_body.position = 400, 500
circle_shape = pymunk.Circle(circle_body, radius)
circle_shape.elasticity = 0.98
circle_shape.friction = 1.0
# Make segment
segment_shape = pymunk.Segment(space.static_body, (0, 60), (800, 0), 2)
segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.98
segment_shape.friction = 1.0
# Add shapes/bodies to space
space.add(circle_body, circle_shape, segment_shape)


@window.event # draw the space when window opens
def on_draw():
    window.clear()
    space.debug_draw(options)


def update(dt):  # Increase physics simulation by one.
    space.step(dt)


if __name__ == "__main__":  # Driver code to update simulation
    pyglet.clock.schedule_interval(update, 1.0 / 60)
    pyglet.app.run()
