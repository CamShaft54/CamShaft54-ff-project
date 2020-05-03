# Project Flow Chart

1. User presses run button on ``Input.py``
2. PySimpleGUI window will open with instructions on what the program does and how to use it.
3. After user closes the first window, a second window will open that will allow the user to enter the size of the gym
(in pixels or meters), the size of the ball (in pixels or centimeters), the user will then choose between showing the
simulation (Option A) or doing it faster behind the scenes (Option B).

## Option A
1. After the user presses submit in the input window, a pyglet window will open from ``Simulation.py``.
2. Inside the window will be two diagonal lines that funnel the ball into an open box.
3. If the user left clicks somewhere in the window, it will spawn a ball at the position.
4. If the user presses ``B`` balls will randomly spawn over the gym until the user presses ``B`` again.
5. If the user presses ``C`` all the balls in the window will be cleared.
6. If the user presses ``T`` a top wall of the gym will be toggled on or off.
7. If the user presses ``D`` all the balls above the top wall will be removed.
8. If the user presses ``A`` auto mode will be activated. This mode will spawn balls randomly (Similarly to pressing``B``)
but will stop when the balls go above the height of the gym. When this happens, the top wall will appear, the balls above
the top wall will be removed, and the number of all balls in the gym will be added to the ``Tests`` array.
9. If the user presses ``M`` the number of balls below the height of the gym will be added to the ``Tests`` array.
10. If the user presses ``F`` the window will close and a PySimpleGUI window with MatPlotLib will open and display a bar
graph showing the results of each test from ``Tests``. 

## Option B
1. When the user presses submit in the input window, the window will close.
2. Another window will open showing the results of each test in a MatPlotLib bar graph.