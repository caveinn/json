import PySimpleGUI as sg
from general_settings_page import window2 as general_settingsWindow
from incoming_settings_page import window2 as incoming_settingsWindow
from json_settings_page import window2 as json_settingsWindow
from delivery_settings_page import window2 as delivery_settingsWindow
from after_effects_settings_page import window2 as effects_settingsWindow
from email_settings_page import window2 as email_settingsWindow

import configparser
config = configparser.ConfigParser()
config.read("app.ini")
# print(config["APP"]["lastCampaign"]["code"])
sg.theme('Dark Grey 5')
sg.theme_input_background_color("darkgrey")
sg.theme_button_color(("white", "black"))
info_column = [
    [sg.T(pad=(50,0))],
    [sg.Col([[
        sg.Text("APP Status", background_color="darkgrey"),
    ],], expand_x=True, background_color="darkgrey", pad=((0), (0)))],
    [sg.Col([[
        sg.Text("Settings",key="-settings-", enable_events=True),
    ],],  expand_x=True)],
    [sg.Col([[
        sg.Text("About"),
    ],], expand_x=True)]
]
logo = data=config["APP"]["logo"]

navigator_column = [
    [sg.Text("Application Running for:", pad=((20,5),(5,5))), sg.Image(data=logo, key="logo", size=(182, 62),)],
    [sg.T(pad=(0,(2)))],
    [sg.Col([[sg.Text("Last Delivered campaign:", pad=((10,0,), (0,20))), sg.Col([
        [sg.Text("00808")],
        [sg.Text("Deleviered: 01.11.2020 @ 10:25am")]
    ])],])],
    [sg.T(pad=(0,(2)))],
    [sg.Text("Last Sync Campaign JSON:"), sg.T("01.11.2020 @ 10:25am")],
    [sg.T(pad=(0,(2)))],
    [sg.Text("Last Sync /Ads folder:",pad=((33,5),(5,5))), sg.T("01.11.2020 @ 10:25am")],
    [sg.T(pad=((5,400),(100,0)))],
    [sg.Text("Sart /stop services:"), sg.Button("stop", key="-stop-")],
    [sg.Text("Automatically start at login"), sg.Checkbox("", key="-autostart-", enable_events=True)],
    [sg.T(pad=(0,2))]

]
# ----- Full layout -----
layout = [
    [
        sg.Column(info_column, vertical_alignment="t", pad=((0,), (15,5))),
        sg.VSeperator(pad=((0, 0), (0, 0),), color="black"),
        sg.Column(navigator_column, vertical_alignment="t", pad=((37,0), (15,5)),),
    ]
]
# Create the window
mainwindow = sg.Window("Support App", layout, margins=(0, 0))

window = mainwindow
# def showNewWindow(window, newWindow):
#     window.hide()
#     window = newWindow
#     window.finalize()
#     window.un_hide()

config = configparser.ConfigParser()


logo_main_white = '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'

config['APP'] ={
    "logo":logo_main_white,
    "lastCampaign_code": "000808",
    "ladtCampaig_date": "randomDate",
    "syncJson": "01.11.2020@10:25am",
    "automaticallyStart": False,
    "services-stopped": True
}

with open ('app.ini', "w") as configFile:
    config.write(configFile)
# config = configparser.ConfigParser()
# config.read("app.ini")
# config["APP"]["logo"] = "updated"
# with open ('app.ini', "w") as configFile:
#     config.write(configFile)


# Create an event loop
stopped = True
while True:
    event, values = window.read()
    # import pdb; pdb.set_trace()
    print(event, values)
    if window == mainwindow:
        stopBtn = window.find_element("-stop-")
        if event == "-stop-":
            stopped = not stopped
            stopBtn.update(
                text="stop" if not stopped else "start",
                button_color="white on red" if not stopped else "white on green"
                )

    if event=="-settings-":
        window.hide()
        window = general_settingsWindow
        window.finalize()
        window.un_hide()
        # showNewWindow(window, general_settingsWindow)
    if event=="-general-":
        window.hide()
        window = general_settingsWindow
        window.finalize()
        window.un_hide()
    if event=="-json-":
        window.hide()
        window = json_settingsWindow
        window.finalize()
        window.un_hide()
    if event=="-email-":
        window.hide()
        window = email_settingsWindow
        window.finalize()
        window.un_hide()
    if event=="-AE-":
        window.hide()
        window = effects_settingsWindow
        window.finalize()
        window.un_hide()
    if event=="-delivery-":
        window.hide()
        window = delivery_settingsWindow
        window.finalize()
        window.un_hide()
    if event=="-incoming-":
        window.hide()
        window = incoming_settingsWindow
        window.finalize()
        window.un_hide()
    if event =="Back":
        window.hide()
        window = mainwindow
        window.un_hide()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        break
