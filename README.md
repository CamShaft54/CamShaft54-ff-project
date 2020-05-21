###### Written by Cameron S., Class of 2023

#### Focus Day: Softballs in the Gym Day
In this project I wanted to make a program that would run simulations of randomly dropping softballs (circles) into
a gym (box). I did this by using the height and width given as the size of the "gym". Then I ran that simulations multiple
times so that there were enough simulations to achieve the total length of the gym. I used the pymunk physics engine and
used pyglet to display the static bodies. In order to make the input windows I used PySimpleGUI and to create the output
graph I used MatPlotLib.

Citations
-
(Note: These are the main websites I used with some of my code being adapted from these):
* Nested Loops: https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops
* Pymunk API Reference: http://www.pymunk.org/en/latest/pymunk.html
* Pymunk Youtube Tutorial: https://youtu.be/pRk---rdrbo
* Pyglet Documentation: https://pyglet.readthedocs.io/en/latest/
* MatPlotLib PyPlot Tutorial: https://matplotlib.org/3.1.0/tutorials/introductory/pyplot.html
* PySimpleGUI Cookbook: https://pysimplegui.readthedocs.io/en/latest/cookbook/

Bugs
-
1. If the user creates a ball with a radius smaller than 0.35m the simulator will glitch because it cannot handle that many
balls, to avoid this don't use enter a ball smaller than that.
2. If the user uses auto mode or auto auto mode, sometimes the box will only fill up 10% with balls before shutting off. This has
temporarily been fixed by removing these outliers from the program, if it is shutting off early, just ignore it.