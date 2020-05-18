# Project Flow Chart

To start the program the user presses the run button on ``OutputGUI.py``. Next an chain of import statements will
start the user at ```InputGUI.py```.

InputGUI.py
-
PySimpleGUI window from ``InputGUI.py`` will open with instructions on what the program does and how to use it.
After the user closes the first window, a second window will open that will allow the user to enter the size of the gym
(in pixels or meters), the size of the ball (in pixels or meters).

focus_day_project.py
-
After the user presses submit in the input window, a pyglet window will open from ``focus_day_project.py``. Inside
the window will be two diagonal lines that funnel the ball into an open box. This is done by making 5 different
bodies and assigning each one to a shape.
#### Mouse and Key presses
In order to use keyboard shortcuts and mouse clicks the ```on_mouse_press``` and ```on_key_press``` functions are used.
Some keyboard shortcuts will delete balls by clearing them from the space, others will activate auto mode and auto auto mode.
Other keyboard shortcuts can be used to manually run simulation, for example clicking the mouse will spawn a ball, pressing "R" 
will manually record the number of balls in the box.
#### Update Function
In order to have the simulation do stuff, the ```update``` function is used. This steps the simulation forward,
if ball spawning is on, spawns balls, if auto mode is on, checks for overflow by comparing two lists every 2 seconds, and if
the overflow shutoff is triggered, it puts the top wall on top of the gym, deletes the balls above, removes the top wall,
then puts it back and deletes the balls above and counts the balls inside the box. This is done to eliminate issues with
cramming too many balls inside the gym to make the simulation more like a real life situation.
#### Tests List
At the end of each round of simulation, the number of balls in the gym (stored in checked_shapes) is appended to the ```tests```
list. In the ```update``` function another function is called which removes outliers in the list.

OutputGUI.py
-
Finally after the simulation is finished, the window will close and the tests array will be passed to OutputGUI.py. This
script defines a function that will create a bar graph of all the simulation recorded. A PySimpleGUI window will also be
created that contains the total number of balls that could fit in the gym and the average number of balls per simulation.