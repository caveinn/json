
import PySimpleGUI as sg
from event_handlers import get_config

sg.theme('Dark Grey 5')
sg.theme_input_background_color("darkgrey")
sg.theme_button_color(("white", "black"))
def make_window():
    config = get_config()
    message = config["EMAIL"]["message"]
    adress = config["EMAIL"]["adress"]
    server = config["EMAIL"]["server"]
    port = config["EMAIL"]["port"]
    username = config["EMAIL"]["username"]
    password = config["EMAIL"]["password"]

    navigator_column = [
        [sg.Col([[
            sg.Text("General", enable_events=True, key="-general-", pad=((20,5), (5,5))),

        ]],  expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("JSON/Ads", enable_events=True, key="-json-",pad=((20,5), (5,5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("Email", background_color="darkgrey",
                    enable_events=True, key="-email-", pad=((20,5), (5,5))),
        ]], background_color="darkgrey", expand_x=True, pad=((0, 0), (0, 0))), ],
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
            sg.B('Back',pad=((20, 10), (250, 0)),button_color=("white", "black"))
        ]], expand_x=True, pad=((0, 0), (0, 20))), ],
    ]



    def create_Text(txt):
        return sg.T(txt, background_color="black", text_color="white")


    info_column = [
        [sg.T("Available Varaibales:"), sg.Column(
            [
                [
                    create_Text("FirstName"), create_Text("LastName"), create_Text("FileLink")
                ],
                [create_Text("ExpiryDate"), create_Text("Reference")]
            ],pad = ((0,0),(5,0)), vertical_alignment="t"
        ),
        ],
        [sg.Text("Mesage:")],
        [
            sg.Multiline(
               message,
                key="message",
                size=(52,10),
            )
        ],
        [sg.T("Email Adress:", pad=((27,5),(10,10))), sg.I(adress, key="adress",size=(37,1))],
        [sg.T("SMTP server:", pad=((27,5),(10,10))), sg.I(server, key="server",size=(20,1)), sg.T("Port:"), sg.I(port,key="port", size=(9,1))],
        [sg.T("SMTP Username:", pad=((7,5),(10,10))), sg.I(username,key="username",size=(38,1))],
        [sg.T("SMTP Passord:",  pad=((18,5),(10,10))), sg.I(password,key="password", size=(38,1),password_char="*")],
        [sg.Text(pad=((405,5),(20)))],
        [sg.B("save", pad=((350, 0), (20, 0)))]

    ]
    # ----- Full layout -----
    layout = [
        [
            sg.Column(navigator_column, vertical_alignment="t", pad=((0,), (15,5))),
            sg.VSeperator(pad=((0, 0), (0, 0),), color="black"),
            sg.Column(info_column, vertical_alignment="t", pad=((30,5), (15,5))),

        ]
    ]
    # Create the window
    window = sg.Window("Settings", layout, margins=(0, 0))
    return window
