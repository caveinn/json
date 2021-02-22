
import PySimpleGUI as sg
sg.theme('Dark Grey 5')
info_column = [
    [
        sg.Text("General", enable_events=True, key="-general-"),

    ],
    [
        sg.Text("JSON/Ads", enable_events=True, key="-json-"),
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
        sg.Text("Server delivery", background_color="darkgrey", enable_events=True, key="-delivery-"),
    ],
    [
        sg.B('Back', pad=((10,10),(250,0)))
    ]
]

navigator_column = [
    [sg.Text("Select Protocal: "), sg.DD(values=["sFTP", "FTP"],)],
    [sg.Text("FTP Server:", pad=((22, 5),(5,5))), sg.I(size=(30,1))],
    [sg.Text("Port:", pad=((57, 5),(5,5))),sg.I(size=(30,1))],
    [sg.Text("Username:", pad=((30, 5),(5,5))), sg.I(size=(30,1))],
    [sg.Text("Password:", pad=((32, 5),(5,5))), sg.I(size=(30,1))],
    [sg.T(pad=((0,400),(70,0)))],
    [sg.T("File Delivery Path:"), sg.I(size=(38,1))],

]
# ----- Full layout -----
layout = [
    [
        sg.Column(info_column,vertical_alignment="t"),
        sg.VSeperator(),
        sg.Column(navigator_column, vertical_alignment="t"),
    ]
]

# Create the window
window2 = sg.Window("Settings", layout)
