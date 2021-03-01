import PySimpleGUI as sg
import configparser
sg.theme('Dark Grey 5')
sg.theme_input_background_color("darkgrey")
sg.theme_button_color(("white", "black"))


def make_window():
    config = configparser.ConfigParser()
    config.read("app.ini")
    app_config = config["APP"]

    # change stop button color
    stopButtonColor = "white on green" if app_config.getboolean(
        "services_stopped") else "white on red"
    stopButtonText = "start" if app_config.getboolean(
        "services_stopped") else "stop"
    navigator_column = [
        [sg.T(pad=(50, 0))],
        [sg.Col([[
            sg.Text("APP Status"),
        ], ], expand_x=True, pad=((0), (0)))],
        [sg.Col([[
            sg.Text("Settings", key="-settings-", enable_events=True),
        ], ],  expand_x=True)],
        [sg.Col([[
            sg.Text("About",  background_color="darkgrey"),
        ], ], expand_x=True,  background_color="darkgrey")]
    ]

    info_column = [
        [sg.Text("Application Running for:", pad=((20, 5), (5, 5))),
         sg.Image(filename=app_config['logo'], key="logo", size=(182, 62),)],
        [sg.T("Concept & Development:"), sg.T("Crealto GmbH")],
        [sg.Column(
            [
                [
                    sg.Column([[sg.T("credits:"), ]], vertical_alignment="t"),

                    sg.Column([
                        [sg.T("Marco Somaini")],
                        [sg.T("Raphael Becker")],
                        [sg.T("Sandra Buhler")],
                        [sg.T("Kevin Nzioka")],
                    ],)
                ]
            ],
            vertical_alignment="t",
            element_justification="t"
        )
        ],
        [sg.Column(
            [
                [
                    sg.Column([[sg.T("Contact:"), ]], vertical_alignment="t"),

                    sg.Column([
                        [sg.T("Crealto GmbH")],
                        [sg.T("aHerrengassli 3")],
                        [sg.T("352 Zaziwil")],
                        [sg.T("Switzerland")],
                        [sg.T(pad=((10, 0)))],
                        [sg.T("www.crealto.ch")],
                        [sg.T("appdev@crealto.ch")],
                    ],)
                ]
            ],
            vertical_alignment="t",
            element_justification="t"
        )
        ],
        [sg.T("App Version:"), sg.T("1.1.2344")],
        [sg.B("Send Email")],

    ]
    # ----- Full layout -----
    layout = [
        [
            sg.Column(navigator_column, vertical_alignment="t",
                      pad=((0,), (15, 5))),
            sg.VSeperator(pad=((0, 0), (0, 0),), color="black"),
            sg.Column(info_column, vertical_alignment="t",
                      pad=((37, 0), (15, 5)),),
        ]
    ]
    # Create the window
    mainwindow = sg.Window("Support App", layout, margins=(0, 0))

    return mainwindow
