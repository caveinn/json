import PySimpleGUI as sg
from settings_page import window2 as settingsWindow

info_column = [
    [
        sg.Text("APP Status"),
    ],
    [
        sg.Text("Settings",key="-settings-", enable_events=True),
    ],
    [
        sg.Text("About"),
    ],
]

navigator_column = [
    [sg.Text("Application Running for:")],
    [sg.Text("Last Delivered campaign")],
    [sg.Text("Last Sync Campaign JSON")],
    [sg.Text("Last Sync /Ads folder", pad=((6,400),(0,400) ))],
    [sg.Text("Sart /stop services:"), sg.Button("stop")],
    [sg.Text("Automatically start at login"), sg.Checkbox("", key="-autostart-", enable_events=True)],
    # [sg.Text(size=(40, 1), key="-TOUT-")],
    # [sg.Image(key="-IMAGE-")],

]
# ----- Full layout -----
layout = [
    [
        sg.Column(info_column,vertical_alignment="t"),
        sg.VSeperator(),
        sg.Column(navigator_column),
    ]
]

# Create the window
window = sg.Window("Support App", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    print(event, values)
    if(event == "-settings-"):
        window.close()
        settingsWindow.read()
    if
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
