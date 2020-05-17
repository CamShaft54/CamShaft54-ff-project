import matplotlib.pyplot as plt
import PySimpleGUI as Sg
from focus_day_project import tests

names = []
for i in range(len(tests)):
    names.append("Sim. #" + str(i))


def draw_plot():
    plt.bar(names, tests)
    plt.show(block=False)


layout = [[Sg.Button('Show Graph'), Sg.Cancel()]]

window = Sg.Window('Final Results', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'Show Graph':
        draw_plot()
window.close()
