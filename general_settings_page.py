
import PySimpleGUI as sg
sg.theme('Dark Grey 5')
sg.theme_input_background_color("darkgrey")
sg.theme_button_color(("white", "black"))

def make_window():
    navigator_column = [
        [sg.Col([[
            sg.Text("General", background_color="darkgrey",
                    enable_events=True, key="-general-",pad=((20,5), (5,5))),
        ]], background_color="darkgrey", expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("JSON/Ads", enable_events=True, key="-json-",pad=((20,5), (5,5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("Email", enable_events=True, key="-email-", pad=((20,5), (5,5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("After Effects",
                    enable_events=True, key="-AE-", pad=((20,5), (5,5))),
        ]],expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("Server Incoming", size=(20, 1), enable_events=True,
                    key="-incoming-",pad=((20,5), (10,5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("Server delivery",
                    enable_events=True, key="-delivery-", pad=((20,5), (5,5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.B('Back',pad=((20, 10), (250, 0)),button_color=("white", "black"), highlight_colors=("red", "green"), use_ttk_buttons=False)
        ]], expand_x=True, pad=((0, 0), (0, 20))), ],
    ]

    info_column = [
        [sg.Text("Upload Logo: "), sg.Text("FILENAME SHOW HERE.jpg", size=(50,1),), sg.FileBrowse("Select",), sg.T(pad=((8,0))) ],
        [sg.Text(pad=((405,5),(0, 170)))],
        [sg.Text("Availability of File online:",pad=((10, 5),(5,5))),sg.I(size=(10,1)), sg.T("Days")],
        [sg.Text("Availability of Master Files:", pad=((0, 5),(5,5))),sg.I(size=(10,1)), sg.T("Days")],
        [sg.Text("Sync Interval FTP:", pad=((37, 5),(5,5))),sg.I(size=(10,1)), sg.T("Minutes")],
        [sg.T(pad=((0,380),(70,0)))],

    ]
    # ----- Full layout -----
    layout = [
        [
            sg.Column(navigator_column, vertical_alignment="t", pad=((0,), (15,5))),
            sg.VSeperator(pad=((0, 0), (0, 0),), color="black"),
            sg.Column(info_column, vertical_alignment="t", pad=((40,0), (15,5)),),
        ]
    ]

    # Create the window
    window = sg.Window("Settings", layout, margins=(0,0))
    return window
