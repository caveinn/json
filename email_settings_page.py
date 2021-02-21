
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


def create_Text(txt):
    return sg.T(txt, background_color="black", text_color="white")


navigator_column = [
    [sg.T("Available Varaibales:"), sg.Column(
        [
            [
                create_Text("FirstName"), create_Text("LastName"), create_Text("FileLink")
            ],
            [create_Text("ExpiryDate"), create_Text("Reference")]
        ],pad = ((0,0),(20,0)), vertical_alignment="t"
    ),
    ],
    [sg.Text("Mesage:")],
    [
        sg.Multiline(
            """
 Dear[fisrt name][last name]

 Your file to tge campaign [reference] is available for download at [file link]

 The link wil expire on [expiry date]

 Best Regars, your APGS|SGA Ad eMotion Team
            """,
            size=(50,10)
        )
    ],
    [sg.T("Email Adress:", pad=((27,5),(10,10))), sg.I(size=(37,1))],
    [sg.T("SMTP server:", pad=((27,5),(10,10))), sg.I(size=(20,1)), sg.T("Port:"), sg.I(size=(9,1))],
    [sg.T("SMTP Username:", pad=((7,5),(10,10))), sg.I(size=(38,1))],
    [sg.T("SMTP Passord:",  pad=((18,5),(10,10))), sg.I(size=(30,1)), sg.B("Show")],
    [sg.T("File Delivery Path:"), sg.I(size=(38,1))],

    # [sg.Text("Sart /stop services:"), sg.Button("stop")],
    # [sg.Text("Automatically start at login"), sg.Checkbox(
    #     "", key="-autostart-", enable_events=True)],
    # [sg.Text(size=(40, 1), key="-TOUT-")],
    # [sg.Image(key="-IMAGE-")],

]
# ----- Full layout -----
layout = [
    [
        sg.Column(info_column, vertical_alignment="t"),
        sg.VSeperator(),
        sg.Column(navigator_column, vertical_alignment="t", justification="c"),
    ]
]

# Create the window
window2 = sg.Window("Settings", layout)
