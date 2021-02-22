
import PySimpleGUI as sg
sg.theme('Dark Grey 5')
info_column = [
    [sg.Col([[
        sg.Text("General", enable_events=True, key="-general-", pad=((20,5), (20,5))),

    ]],  expand_x=True, pad=((0, 0), (0, 0))), ],
    [sg.Col([[
        sg.Text("JSON/Ads", enable_events=True, key="-json-",pad=((20,5), (5,5))),
    ]], expand_x=True, pad=((0, 0), (0, 0))), ],
    [sg.Col([[
        sg.Text("Email", enable_events=True, key="-email-", pad=((20,5), (5,5))),
    ]], expand_x=True, pad=((0, 0), (0, 0))), ],
    [sg.Col([[
        sg.Text("After Effects", background_color="darkgrey",
                enable_events=True, key="-AE-", pad=((20,5), (5,5))),
    ]], background_color="darkgrey", expand_x=True, pad=((0, 0), (0, 0))), ],
    [sg.Col([[
        sg.Text("Server Incoming", size=(20, 1), enable_events=True,
                key="-incoming-",pad=((20,5), (10,5))),
    ]], expand_x=True, pad=((0, 0), (0, 0))), ],
    [sg.Col([[
        sg.Text("Server delivery", enable_events=True, key="-delivery-" ,pad=((20,5), (5,5))),
    ]], expand_x=True, pad=((0, 0), (0, 0))), ],
    [sg.Col([[
        sg.B('Back',pad=((20, 10), (250, 0)),button_color=("white", "black"), highlight_colors=("red", "green"), use_ttk_buttons=False)
    ]], expand_x=True, pad=((0, 0), (0, 20))), ],
]

navigator_column = [
    [sg.Text("Select AfterEffects Project:"), sg.Text(
        "//show path here"),  sg.Button("select")],
    [sg.Text("Select Render:", pad=((60, 5), (0, 0))),
     sg.Text("//show path here"), sg.Button("select")],
    [sg.Text("Select Backup Path:", pad=((35, 5), (0, 0))),
     sg.Text("//show path here"),  sg.Button("select")],
    [sg.Text("", pad=((6, 400), (0, 300)))],

]
# ----- Full layout -----
layout = [
    [
        sg.Column(info_column, vertical_alignment="t",
                  justification="right", pad=((0,), (0))),
        sg.VSeperator(pad=((0, 0), (0, 0))),
        sg.Column(navigator_column, justification="right"),
    ]
]

# Create the window
window2 = sg.Window("Settings", layout, margins=(0, 0))
