
import PySimpleGUI as sg
from utils import get_config
from output import apg_logo

sg.theme_input_background_color("darkgrey")
sg.theme_button_color(("white", "black"))


def make_window():
    config = get_config()["INCOMING"]

    navigator_column = [
        [sg.Col([[
            sg.Text("General", enable_events=True,
                    key="-general-", pad=((20, 5), (5, 5))),

        ]],  expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("JSON/Ads", enable_events=True,
                    key="-json-", pad=((20, 5), (5, 5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("Email", enable_events=True,
                    key="-email-", pad=((20, 5), (5, 5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("After Effects",
                    enable_events=True, key="-AE-", pad=((20, 5), (5, 5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("Server Incoming", background_color="darkgrey", size=(20, 1),
                    enable_events=True, key="-incoming-", pad=((20, 5), (5, 5))),
        ]], background_color="darkgrey", expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.Text("Server delivery",
                    enable_events=True, key="-delivery-", pad=((20, 5), (5, 5))),
        ]], expand_x=True, pad=((0, 0), (0, 0))), ],
        [sg.Col([[
            sg.B('Back', pad=((20, 10), (250, 0)), button_color=(
                "white", "black"), highlight_colors=("red", "green"), use_ttk_buttons=False)
        ]], expand_x=True, pad=((0, 0), (0, 20))), ],
    ]
    info_column = [
        [sg.Text("Select Protocal: "), sg.DD(values=["sFTP", "FTP"],
                                             key="protocal", default_value=config["protocal"], enable_events=True)],
        [sg.Text("FTP Server:" if config["protocal"] == 'FTP' else "sFTP server", pad=(
            (22, 5), (5, 5)), key="server_ident"), sg.I(config["server"], key="server", size=(30, 1))],
        [sg.Text("Port:", pad=((57, 5), (5, 5))), sg.I(
            config["port"], key="port", size=(30, 1))],
        [sg.Text("Username:", pad=((30, 5), (5, 5))), sg.I(
            config["username"], key="username", size=(30, 1))],
        [sg.Text("Password:", pad=((32, 5), (5, 5)), key="password_ident"), sg.I(
            config["password"], size=(30, 1), key="password", password_char="*", disabled= not config["protocal"] == 'FTP'),],
        [sg.Text("path to private key" if not config.get("private_key_path") else config.get("private_key_path"), size=(40, 1), pad=(
            (32, 5), (5, 5))), sg.FileBrowse("Private Key", disabled=config["protocal"] == 'FTP', key="private_key_path")],
        [sg.T(pad=((0, 400), (70, 0)))],
        [sg.T("Campaign JSON path:"), sg.I(
            config["json_path"], key="json_path", size=(20, 1),)],
        [sg.T("Campaign Ads path:", pad=((15, 5), (5, 5))), sg.I(
            config["ads_path"], key="ads_path", size=(20, 1),)],
        [sg.B("save", pad=((280, 20), (140, 5)))]

    ]
    # ----- Full layout -----
    layout = [
        [
            sg.Column(navigator_column, vertical_alignment="t",
                      pad=((0,), (15, 5))),
            sg.VSeperator(pad=((0, 0), (0, 0),), color="black"),
            sg.Column(info_column, vertical_alignment="t",
                      pad=((0,), (15, 5)),),
        ]
    ]

    # Create the window
    window = sg.Window("Settings", layout, margins=(0, 0), icon=apg_logo)
    return window
