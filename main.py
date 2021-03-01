import PySimpleGUI as sg
from general_settings_page import make_window as general_settingsWindow
from incoming_settings_page import make_window as incoming_settingsWindow
from json_settings_page import make_window as json_settingsWindow
from delivery_settings_page import make_window as delivery_settingsWindow
from after_effects_settings_page import make_window as effects_settingsWindow
from email_settings_page import make_window as email_settingsWindow
from app_status_page import make_window as mainwindow
from about_page import make_window as aboutwindow
from utils import init_config_file
from event_handlers import(
    main_event_handler,
    general_settings_event_handler,
    json_settings_event_handler,
    email_settings_event_handler
)


init_config_file()

window = mainwindow()
current_window = "main"
while True:
    event, values = window.read()
    # import pdb; pdb.set_trace()
    print(event, values)
    if current_window == "main":
        main_event_handler(event, values, window)
    elif current_window == "general":
        general_settings_event_handler(event, values, window)
    elif current_window == "json":
        json_settings_event_handler(event, values, window)
    elif current_window == "email":
        email_settings_event_handler(event, values, window)

    if event == "-settings-":
        current_window = "general"
        window.hide()
        window = general_settingsWindow()
        window.finalize()
        window.un_hide()
        # showNewWindow(window, general_settingsWindow)
    if event == "-general-":
        current_window = "general"
        window.hide()
        window = general_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "-json-":
        current_window = "json"
        window.hide()
        window = json_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "-email-":
        current_window = "email"
        window.hide()
        window = email_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "-AE-":
        window.hide()
        window = effects_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "-delivery-":
        window.hide()
        window = delivery_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "-incoming-":
        window.hide()
        window = incoming_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "Back":
        current_window="main"
        window.hide()
        window = mainwindow()
        window.finalize()
        window.un_hide()
    if event == "About":
        current_window = "about"
        window.hide()
        window = aboutwindow()
        window.finalize()
        window.un_hide()

    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        break
