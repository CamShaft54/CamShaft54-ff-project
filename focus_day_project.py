import pymunk
import time

space = pymunk.Space()
space.gravity = 0, -1000
body = pymunk.Body(1, 1666)
body.position = 50, 100

space.add(body)

while True:
    space.step(0.02)  # 50 fps
    print(body.position)
    time.sleep(0.5)
