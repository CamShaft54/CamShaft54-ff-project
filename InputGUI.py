import PySimpleGUI as Sg
import sys

"""DO NOT RUN THIS PROGRAM! RUN OutputGUI.py INSTEAD!"""


def instructions():  # Make instructions window
    instructions_layout = [  # Define layout of instructions window.
        [Sg.Text("Welcome to Softballs in the Gym Day Simulator!")],
        [Sg.Text(
            "In this simulator you can specify the dimensions of a gym and the size of the softball to run a visual "
            "simulation.")],
        [Sg.Text("Here are the keyboard shortcuts for the simulator:")],
        [Sg.Text("A: Auto Mode, spawns balls automatically until the balls reach the top of the gym.")],
        [Sg.Text("Q: Auto Auto Mode, activates auto mode and when auto mode completes it restarts again.")],
        [Sg.Text("B: Ball Spawning, randomly spawns balls above the gym, press B again to turn off.")],
        [Sg.Text("C: Clear Balls, clears all balls in simulation.")],
        [Sg.Text("D: Clear Extraneous Balls, clears all balls above the gym.")],
        [Sg.Text("F: Finish, closes window, prints tests results.")],
        [Sg.Text(
            "R: Record, manually record the current number of balls in gyms and add value to the final tests list.")],
        [Sg.Text("S: Speed up simulation (can be buggy).")],
        [Sg.Text("T: Toggle Top Wall, adds or removes the top wall of the gym.")],
        [Sg.Text("Mouse Click: Spawns ball at mouse coordinate.")],
        [Sg.Text("Note: due to constraints of the physics engine used, using a ball with a radius less than 0.35m will "
                 "not work. A fix may be available in the future for this.")],
        [Sg.Button('Continue', key='instructions_continue'), Sg.Cancel()]
    ]
    instructions_window = Sg.Window('Welcome', instructions_layout)
    while True:
        event, values = instructions_window.read()
        if event == 'instructions_continue':
            instructions_window.close()
            break
        if event in (None, 'Cancel'):
            sys.exit()


def input_window():  # Create an Input Window
    input_layout = [  # Define layout of input window.
        [Sg.Text("The width and height are the two values used to make the 2D gym in the simulation.")],
        [Sg.Text("The number of simulations is determined by the length and radius of the softball.")],
        [Sg.Text("If you are unsure of what to do, just use the default values already entered")],
        [Sg.Text("and press the Q key to start the auto simulation. If you don't want to wait a long time")],
        [Sg.Text(" change the length of the gym to a smaller number. Also, when the simulation opens,")],
        [Sg.Text("try pressing the ` key (top left of keyboard).")],
        [Sg.Text("Units: "), Sg.Radio("Meters", group_id='units', key='m', default=True),
         Sg.Radio("Pixels", group_id='units', key='p')],
        [Sg.Text("Width of Gym: "), Sg.Input("15", key='width', size=(5, 1)), Sg.Text("Height of Gym"),
         Sg.Input("7", key='height', size=(5, 1))],
        [Sg.Text("Length of Gym: "), Sg.Input("28", key='length', size=(5, 1))],
        [Sg.Text("Softball Radius: "), Sg.Input("0.35", key='softball', size=(5, 1))],
        [Sg.Text("If you entered a ball radius less than 0.35m (350px) then select the multiple simulations per section"
                 " option below.")],
        [Sg.Text("Multiple Simulations Mode:"), Sg.Radio("On", group_id='multi_mode', key='multi_on'),
         Sg.Radio("Off", group_id='multi_mode', key='multi_off')],
        [Sg.Button("Submit", key='submit', bind_return_key=True), Sg.Cancel()]
    ]
    input_win = Sg.Window('Input', input_layout)
    while True:
        event, values = input_win.read()
        if event in (None, 'Cancel'):  # If user closes window, kill program.
            sys.exit()
        if event == 'submit':
            input_win.close()
            if float(values['softball']) == 3.1415:
                exec(open('Setup.py', encoding="utf-8").read(), globals())
            elif values['m']:  # If metric, convert values to pixels, otherwise only calculate # of simulations needed.
                return [int(float(values['width']) * 1000), int(float(values['height']) * 1000),
                        int(float(values['length']) / (2 * float(values['softball']))),
                        int(float(values['softball']) * 1000), values['multi_on']]
            return [int(values['width']), int(values['height']),
                    int(float(values['length']) / (2 * float(values['softball']))), int(values['softball']),
                    values['multi_on']]


# Driver Code
instructions()
user_input = input_window()
