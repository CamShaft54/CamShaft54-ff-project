import pyglet

window = pyglet.window.Window(1280, 720, "Pymunk Testing", resizable=False)


@window.event
def on_draw():
    window.clear()


def update(dt):
    pass


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0 / 60)
    pyglet.app.run()
