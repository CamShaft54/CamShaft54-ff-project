import PySimpleGUI as Sg


def instructions():
    instructions_layout = [
        [Sg.Text("Welcome to Softballs in the Gym Day Simulator!")],
        [Sg.Text(
            "In this simulator you can specify the dimensions of a gym and the size of the softball to run a visual "
            "simulation.")],
        [Sg.Text("Here are the keyboard shortcuts for the simulator:")],
        [Sg.Text("A: Auto Mode, spawns balls automatically until the balls reach the top of the gym.")],
        [Sg.Text("HOME: Auto Auto Mode, activates auto mode and when auto mode completes it restarts again.")],
        [Sg.Text("B: Ball Spawning, randomly spawns balls above the gym, press B again to turn off.")],
        [Sg.Text("C: Clear Balls, clears all balls in simulation.")],
        [Sg.Text("D: Clear Extraneous Balls, clears all balls above the gym.")],
        [Sg.Text("F: Finish, closes window, prints tests results.")],
        [Sg.Text(
            "R: Record, manually record the current number of balls in gyms and add value to the final tests list.")],
        [Sg.Text("T: Toggle Top Wall, adds or removes the top wall of the gym.")],
        [Sg.Text("Mouse Click: Spawns ball at mouse coordinate.")],
        [Sg.Button('Hello', key='instructions_continue'), Sg.Cancel()]
    ]
    instructions_window = Sg.Window('Welcome', instructions_layout)
    while True:
        event, values = instructions_window.read()
        if event in (None, 'Cancel'):
            break
        if event == 'instructions_continue':
            instructions_window.close()


def input_window():
    input_layout = [
        [Sg.Text("Units: "), Sg.Radio("Meters", group_id='units', key='m', default=True),
         Sg.Radio("Pixels", group_id='units', key='p')],
        [Sg.Text("Width of Gym: "), Sg.Input("15", key='width'), Sg.Text("Height of Gym"),
         Sg.Input("7", key='height')],
        [Sg.Text("Length of Gym: "), Sg.Input("28", key='length')],
        [Sg.Text("Softball Radius: "), Sg.Input("0.7", key='softball')],
        [Sg.Button("Submit", key='submit'), Sg.Cancel()]
    ]
    input_win = Sg.Window('Input', input_layout)
    while True:
        event, values = input_win.read()
        if event in (None, 'Cancel'):
            break
        if event == 'submit':
            print("Submit input window")
            if values['m']:
                return [int(float(values['width']) * 1000), int(float(values['height']) * 1000), int(float(values['length']) * 1000)
                        , int(float(values['softball']) * 1000)]
            return [int(values['width']), int(values['height']), int(values['length']), int(values['softball'])]


if __name__ == "__main__":
    instructions()
    user_input = input_window()
    print(user_input)
    print(user_input)
user_input = None
