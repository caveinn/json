import configparser
from utils import is_image
import PySimpleGUI as sg

def write_config(config):
    with open('app.ini', "w") as configFile:
        config.write(configFile)

def get_config():
    config = configparser.ConfigParser()
    config.read("app.ini")
    return config


def main_event_handler(event,values, window):
    config = get_config()
    stopBtn = window.find_element("-stop-")

    if event == "-stop-":

        stopped = not config.getboolean("APP","services_stopped")
        config["APP"]["services_stopped"] = str(stopped)
        write_config(config)
        stopBtn.update(
            text="stop" if not stopped else "start",
            button_color="white on red" if not stopped else "white on green"
            )
    if event == "-autostart-":
        config["APP"]["automaticallystart"] = str(values[event])
        write_config(config)

def general_settings_event_handler(event,values, window):
    config = get_config()
    if event == "save":
        logo = values["Select"]
        if is_image(logo):
            config["APP"]["logo"] = logo
        elif logo != '':
            sg.Popup("Logo not saved because it is not an image")
        try:
            int(values[1])
            int(values[2])
            int(values[3])

            config["GENERAL"]["online_availability_duration"] = values[1]
            config["GENERAL"]["master_availability_duration"] = values[2]
            config["GENERAL"]["sync_interval"] = values[3]
        except Exception as e:
            print(e)
            sg.popup("online_availability_duration,master_availability_duration, sync_interval must be interger values ")

        write_config(config)


def json_settings_event_handler(event,values, window):
    config = get_config()
    if event == "save":
        config["ADS"]["campaign_json_path"] = values["campaign"]
        config["ADS"]["ae_file"] = values["ae"]
        config["ADS"]["ads"] = values["ads"]
    write_config(config)
