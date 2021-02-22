import PySimpleGUI as sg
from general_settings_page import window2 as general_settingsWindow
from incoming_settings_page import window2 as incoming_settingsWindow
from json_settings_page import window2 as json_settingsWindow
from delivery_settings_page import window2 as delivery_settingsWindow
from after_effects_settings_page import window2 as effects_settingsWindow
from email_settings_page import window2 as email_settingsWindow


info_column = [
    [
        sg.Text("APP Status"),
    ],
    [
        sg.Text("Settings",key="-settings-", enable_events=True),
    ],
    [
        sg.Text("About"),
    ],
]

navigator_column = [
    [sg.Text("Application Running for:")],
    [sg.Text("Last Delivered campaign")],
    [sg.Text("Last Sync Campaign JSON")],
    [sg.Text("Last Sync /Ads folder", pad=((6,400),(0,400) ))],
    [sg.Text("Sart /stop services:"), sg.Button("stop")],
    [sg.Text("Automatically start at login"), sg.Checkbox("", key="-autostart-", enable_events=True)],

]
# ----- Full layout -----
layout = [
    [
        sg.Column(info_column,vertical_alignment="t"),
        sg.VSeperator(),
        sg.Column(navigator_column),
    ]
]

# Create the window
mainwindow = sg.Window("Support App", layout)
window = mainwindow
# def showNewWindow(window, newWindow):
#     window.hide()
#     window = newWindow
#     window.finalize()
#     window.un_hide()
# Create an event loop
while True:

    event, values = window.read()
    print(event, values)
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
    if event =="Back":
        window.hide()
        window = mainwindow
        window.un_hide()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        break
