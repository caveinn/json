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
            sg.Text("APP Status", background_color="darkgrey"),
        ], ], expand_x=True, background_color="darkgrey", pad=((0), (0)))],
        [sg.Col([[
            sg.Text("Settings", key="-settings-", enable_events=True),
        ], ],  expand_x=True)],
        [sg.Col([[
            sg.Text("About"),
        ], ], expand_x=True)]
    ]

    info_column = [
        [sg.Text("Application Running for:", pad=((20, 5), (5, 5))),
         sg.Image(filename=app_config['logo'], key="logo", size=(182, 62),)],
        [sg.T(pad=(0, (2)))],
        [sg.Col([[sg.Text("Last Delivered campaign:", pad=((10, 0,), (0, 20))), sg.Col([
            [sg.Text(app_config['lastcampaign_code'])],
            [sg.Text(app_config['lastCampaign_date'])]
        ])], ])],
        [sg.T(pad=(0, (2)))],
        [sg.Text("Last Sync Campaign JSON:"), sg.T(app_config['syncjson'])],
        [sg.T(pad=(0, (2)))],
        [sg.Text("Last Sync /Ads folder:", pad=((33, 5), (5, 5))),
         sg.T(app_config['sync_folder'])],
        [sg.T(pad=((5, 400), (100, 0)))],
        [sg.Text("Sart /stop services:"), sg.Button(stopButtonText, key="-stop-",button_color=stopButtonColor)],
        [sg.Text("Automatically start at login"), sg.Checkbox(
            "", key="-autostart-", enable_events=True, default=True if app_config.getboolean('automaticallystart') else False)],
        [sg.T(pad=(0, 2))]

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
