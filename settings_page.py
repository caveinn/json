
import PySimpleGUI as sg
info_column = [
    [
        sg.Text("General"),
    ],
    [
        sg.Text("JSON/Ads"),
    ],
    [
        sg.Text("Email"),
    ],
    [
        sg.Text("After Effects"),
    ],
    [
        sg.Text("Server Incoming"),
    ],
    [
        sg.Text("Server delivery"),
    ],
]

navigator_column = [
    [sg.Text("Upload Logo: "), sg.Button("select")],
    [sg.Text("Upload Icon"), sg.Button("select")],
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
window2 = sg.Window("Settings", layout)
