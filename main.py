import PySimpleGUI as sg


info_column = [
    [
        sg.Text("APP Status"),
    ],
    [
        sg.Text("Settings"),
    ],
    [
        sg.Text("About"),
    ],
]

navigator_column = [
    [sg.Text("Application Running for:")],
    [sg.Text("Last Delivered campaign")],
    [sg.Text("Last Sync Campaign JSON")],
    [sg.Text("Last Sync /Ads folder")],
    [sg.T("", (40,50))],
    [sg.Text("Sart /stop services:"), sg.Button("stop")],
    [sg.Text("Automatically start at login"), sg.Checkbox("")],
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
window = sg.Window("Support App", layout, resizable=True)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
