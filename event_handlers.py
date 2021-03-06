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


def main_event_handler(event,values, window, services):
    config = get_config()
    stopBtn = window.find_element("-stop-")

    if event == "-stop-":

        stopped = config.getboolean("APP","services_stopped")
        stopped = not stopped
        config["APP"]["services_stopped"] = str(stopped)

        write_config(config)
        stopBtn.update(
            text="stop" if not stopped else "start",
            button_color="white on red" if not stopped else "white on green"
            )
        if not stopped:
            services.run_services()
    if event == "-autostart-":
        config["APP"]["automaticallystart"] = str(values[event])
        write_config(config)
    keys = [
    "lastcampaign_code",
    "lastcampaign_date",
    "syncjson",
    "sync_folder"
    ]
    for key in keys:
        to_update = window.find_element(key)
        to_update.update(config["APP"][key])

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
        config["ADS"]["campaign_json_path"] = values["campaign"] if values["campaign"] else config["ADS"]["campaign_json_path"]
        config["ADS"]["ae_file"] = values["ae"] if values["ae"] else config["ADS"]["ae_file"]
        config["ADS"]["ads"] = values["ads"] if values["ads"] else config["ADS"]["ads"]
    write_config(config)

def email_settings_event_handler(event,values, window):
    config = get_config()
    if event == "save":
       for k,v in values.items():
           config["EMAIL"][k] = v if  v else config["EMAIL"][k]
    write_config(config)

def incoming_settings_event_handler(event, values, window):
    config = get_config()
    if event == "protocal":
        print(values)
        window.Element("server_ident").Update("FTP Server:" if values["protocal"]  == 'FTP' else "sFTP server")
        window.Element("private_key_path").Update(disabled=values["protocal"]  == 'FTP' )
        window.Element("password").Update(disabled=not values["protocal"]  == 'FTP')
    if event == "save":
        if not values['private_key_path'].endswith('pem') and values['protocal'] == 'sFTP':
            config["ERRORS"]["json_error"] += "\n Kindly provide a private key file of .pem"
            write_config(config)
            return

        for k,v in values.items():
           config["INCOMING"][k] = v if v else config["INCOMING"][k]
    write_config(config)

def delivery_settings_event_handler(event, values, window):
    config = get_config()
    if event == "protocal":
        print(values)
        window.Element("server_ident").Update("FTP Server:" if values["protocal"]  == 'FTP' else "sFTP server")
        window.Element("private_key_path").Update(disabled=values["protocal"]  == 'FTP' )
        window.Element("password").Update(disabled=not values["protocal"]  == 'FTP')
    if event == "save":
        if not values['private_key_path'].endswith('pem') and values['protocal'] == 'sFTP':
            config["ERRORS"]["json_error"] += "\n Kindly provide a private key file of .pem"
            write_config(config)
            return
    if event == "save":
       for k,v in values.items():
           config["DELIVERY"][k] = v if v else config["DELIVERY"][k]
    write_config(config)

def ae_settings_event_handler(event, values, widnow):
    config = get_config()
    if event == "save":
       for k,v in values.items():
           config["AE"][k] = v if v else config["AE"][k]
    write_config(config)
