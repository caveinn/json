
import PySimpleGUI as sg
sg.theme_input_background_color("darkgrey")
sg.theme_button_color(("white", "black"))
def make_window():
    navigator_column = [
        [sg.Col([[
            sg.Text("General", enable_events=True, key="-general-", pad=((20,5), (5,5))),

        ]],  expand_x=True, pad=((0, 0), (0, 0))), ],
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
            sg.Text("Server delivery", background_color="darkgrey",
                    enable_events=True, key="-delivery-", pad=((20,5), (5,5))),
        ]], background_color="darkgrey", expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.B('Back',pad=((20, 10), (250, 0)),button_color=("white", "black"), highlight_colors=("red", "green"), use_ttk_buttons=False)
        ]], expand_x=True, pad=((0, 0), (0, 20))), ],
    ]

    info_column = [
        [sg.Text("Select Protocal: "), sg.DD(values=["sFTP", "FTP"],)],
        [sg.Text("FTP Server:", pad=((22, 5), (5, 5))), sg.I(size=(30, 1))],
        [sg.Text("Port:", pad=((57, 5), (5, 5))), sg.I(size=(30, 1))],
        [sg.Text("Username:", pad=((30, 5), (5, 5))), sg.I(size=(30, 1))],
        [sg.Text("Password:", pad=((32, 5), (5, 5))), sg.I(size=(30, 1))],
        [sg.T(pad=((0, 400), (70, 0)))],
        [sg.T("File Delivery Path:"), sg.I(size=(38, 1))],

    ]
    # ----- Full layout -----
    layout = [
        [
            sg.Column(navigator_column, vertical_alignment="t", pad=((0,), (15,5))),
            sg.VSeperator(pad=((0, 0), (0, 0),), color="black"),
            sg.Column(info_column, vertical_alignment="t", pad=((0,), (15,5)),),
        ]
    ]

    # Create the window
    window = sg.Window("Settings", layout, margins=(0,0))
    return window
