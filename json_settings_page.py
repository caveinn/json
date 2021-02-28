
import PySimpleGUI as sg
from event_handlers import get_config
sg.theme('Dark Grey 5')
sg.theme_input_background_color("darkgrey")
sg.theme_button_color(("white", "black"))
def make_window():
    config = get_config()
    campaign_path = config["ADS"]["campaign_json_path"]
    ae_path = config["ADS"]["ae_file"]
    ads = config["ADS"]["ads"]

    navigator_column = [
        [sg.Col([[
            sg.Text("General", enable_events=True, key="-general-", pad=((20,5), (5,5))),

        ]],  expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("JSON/Ads", background_color="darkgrey",
                    enable_events=True, key="-json-", pad=((20,5), (5,5))),
        ]], background_color="darkgrey", expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("Email", enable_events=True, key="-email-", pad=((20,5), (5,5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("After Effects",
                    enable_events=True, key="-AE-", pad=((20,5), (5,5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
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



    info_column = [
        [sg.Text("Campaign JSON Path:", pad=((7,5),(0,0))),sg.Text(campaign_path, size=(50,1)),  sg.FolderBrowse("select", key="campaign")],
        [sg.Text("After Effects JSON file:"), sg.Text(ae_path, size=(50,1)), sg.FolderBrowse("select", key="ae")],
        [sg.Text("Campaign Ads Path: ", pad=((17,5),(0,0))),sg.Text(ads, size=(50,1)),  sg.FolderBrowse("select", key='ads')],
        [sg.Text(pad=((505,5),(0, 170)))],
        [sg.Button("save", pad=((440,0), (120,5)))]

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
    window = sg.Window("Settings", layout, margins=(0, 0))
    return window
