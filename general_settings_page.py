
import PySimpleGUI as sg
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
        sg.Text("Server delivery", enable_events=True, key="-delivery-"),
    ],
    [
        sg.B('Back', pad=((10,10),(250,0)))
    ]
]

navigator_column = [
    [sg.Text("Upload Logo: "), sg.Text("FILENAME SHOW HERE.jpg", size=(30,1)), sg.B("Select") ],
    [sg.Text("Upload Icon: ",pad=((10,5),(5))), sg.Text("FILENAME SHOW HERE.jpg", size=(30,1)), sg.B("select")],
    [sg.Text(pad=((405,5),(0, 170)))],
    [sg.Text("Availability of File online:", pad=((10, 5),(5,5))),sg.I(size=(10,1)), sg.T("Days")],
    [sg.Text("Availability of Master Files:", pad=((0, 5),(5,5))),sg.I(size=(10,1)), sg.T("Days")],
    [sg.Text("Sync Intervall FTP:", pad=((35, 5),(5,5))),sg.I(size=(10,1)), sg.T("Minutes")],
    [sg.T(pad=((0,400),(70,0)))],

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
