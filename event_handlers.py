import configparser

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
