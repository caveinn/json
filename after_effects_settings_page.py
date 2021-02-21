
import PySimpleGUI as sg
info_column = [
    [
        sg.Text("General", enable_events=True, key="-general-"),

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
    [
        sg.B('Back', pad=((10,10),(250,0)))
    ]
]

navigator_column = [
    [sg.Text("Select AfterEffects Project:"),sg.Text("//show path here"),  sg.Button("select")],
    [sg.Text("Select Render"), sg.Text("//show path here"), sg.Button("select")],
    [sg.Text("Select Backup Path: "),sg.Text("//show path here"),  sg.Button("select")],
    [sg.Text("", pad=((6,400),(0,300) ))],

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
