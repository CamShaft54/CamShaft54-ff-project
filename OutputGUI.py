import matplotlib.pyplot as plt
import PySimpleGUI as Sg
from focus_day_project import tests
'''RUN THIS PROGRAM!'''


def draw_plot():  # Make bar graph
    plt.bar(names, tests)
    plt.show(block=False)


if len(tests) > 0:  # If user does not record any tests average ball count won't be calculated to prevent errors
    average_ball_count = str(round(sum(tests) / len(tests)))
else:
    average_ball_count = "N/A"

names = []
for i in range(len(tests)):  # Create labels for each simulation
    names.append("Sim. #" + str(i + 1))

layout = [  # Layout of output window
    [Sg.Text("Simulation Complete!")],
    [Sg.Text("Average ball count: " + average_ball_count),
     Sg.Text("Total ball count: " + str(sum(tests)))],
    [Sg.Button('Show Graph'), Sg.Cancel()]
]

window = Sg.Window('Final Results', layout)  # create window

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # If user closes window stop program.
        break
    elif event == 'Show Graph':  # If user presses show graph open MatPlotLib simulation
        draw_plot()
window.close()
