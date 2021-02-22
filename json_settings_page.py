
import PySimpleGUI as sg
sg.theme('Dark Grey 5')
info_column = [
    [
        sg.Text("General", enable_events=True, key="-general-"),

    ],
    [
        sg.Text("JSON/Ads", background_color="darkgrey", enable_events=True, key="-json-"),
    ],
    [
        sg.Text("Email", enable_events=True, key="-email-"),
    ],
    [
        sg.Text("After Effects", enable_events=True, key="-AE-"),
    ],
    [
        sg.Text("Server Incoming", enable_events=True, key="-incoming-"),
    ],
    [
        sg.Text("Server delivery", enable_events=True, key="-delivery-"),
    ],
    [
        sg.B('Back', pad=((10,10),(250,0)))
    ]
]


navigator_column = [
    [sg.Text("Campaign JSON Path:", pad=((7,5),(0,0))),sg.Text("//show path here"),  sg.Button("select")],
    [sg.Text("After Effects JSON file:"), sg.Text("//show path here"), sg.Button("select")],
    [sg.Text("Campaign Ads Path: ", pad=((17,5),(0,0))),sg.Text("//show path here"),  sg.Button("select")],
    [sg.Text(pad=((405,5),(0, 170)))],

]
# ----- Full layout -----
layout = [
    [
        sg.Column(info_column,vertical_alignment="t"),
        sg.VSeperator(),
        sg.Column(navigator_column,vertical_alignment="t"),
    ]
]

# Create the window
window2 = sg.Window("Settings", layout)
