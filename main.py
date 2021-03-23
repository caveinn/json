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
from event_handlers import (
    delivery_settings_event_handler,
    email_settings_event_handler,
    general_settings_event_handler,
    incoming_settings_event_handler,
    json_settings_event_handler,
    main_event_handler,
    ae_settings_event_handler,
)
from utils import Services, get_config, write_config
import threading
from output import apg_logo


init_config_file()

window = mainwindow()
current_window = "main"

my_service = Services()
# def run_services():
#     my_service.run_services()

config = get_config()
stopped = config.getboolean("APP","services_stopped")
if not stopped:
    my_service.run_services()


def display_errors():
    try:
        config = get_config()
        if config["ERRORS"]["json_error"]:
            sg.Popup(config["ERRORS"]["json_error"],title="Error")
            config["ERRORS"]["json_error"] = ''
            write_config(config)
    except Exception as e:
        print(e)

while True:
    display_errors()
    event, values = window.read(timeout=100)
    # import pdb; pdb.set_trace()

    if current_window == "main":
        main_event_handler(event, values, window, my_service)
        display_errors()
    elif current_window == "general":
        general_settings_event_handler(event, values, window)
        display_errors()
    elif current_window == "json":
        json_settings_event_handler(event, values, window)
        display_errors()
    elif current_window == "email":
        email_settings_event_handler(event, values, window)
        display_errors()
    elif current_window == "incoming":
        incoming_settings_event_handler(event, values, window)
        display_errors()
    elif current_window == "delivery":
        delivery_settings_event_handler(event, values, window)
        display_errors()
    elif current_window == "AE":
        ae_settings_event_handler(event, values, window)
        display_errors()

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
        current_window = "AE"
        window.hide()
        window = effects_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "-delivery-":
        current_window = "delivery"
        window.hide()
        window = delivery_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "-incoming-":
        current_window = "incoming"
        window.hide()
        window = incoming_settingsWindow()
        window.finalize()
        window.un_hide()
    if event == "Back":
        current_window = "main"
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

    display_errors()

    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        break

config = get_config()
stopped = config.getboolean("APP","services_stopped")
config["APP"]["services_stopped"] = str(True)
write_config(config)
