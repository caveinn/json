import threading
import configparser
import os


class Services():
    pass


def init_config_file():
    if os.path.exists("app.ini"):
        return
    config = configparser.ConfigParser()
    config['APP'] = {
        "logo": '',
        "lastCampaign_code": "000808",
        "ladtCampaig_date": "randomDate",
        "syncJson": "01.11.2020@10:25am",
        "automaticallyStart": False,
        "services-stopped": True
    }
    config['GENERAL'] = {
        "online_availability_duration": 1,
        "master_availability_duration": 1,
        "sync interval": 5,
    }
    config["ADS"] ={
        "campaign_JSON_path": "~/Desktop/campaign",
        "AE_file": "~/Desktop/AEjson",
        "ADs": "~/Desktop/ads"
    }

    config["EMAIL"]={
        "message": '''
 Dear[fisrt name][last name]

 Your file to the campaign [reference] is available for download at [file link]

 The link wil expire on [expiry date]

 Best Regars, your APGS|SGA Ad eMotion Team
        ''',
        "adress": "example@example.com",
        "server": "127.0.0.1",
        "port":"8080",
        "usernmae": "example",
        "password": "sample"
    }

    config["AE"] = {
        "project": "path here",
        "render": "path here",
        "backup_path":" path here",
            }
    config["DELIVERY"] ={
        "protocal": "FTP",
        "server": "127.0.0.1",
        "port": 8080,
        "usernane": "name",
        "password": "sample",
        "delivery_path": "path_here"
    }

    config["INCOMING"] ={
        "protocal": "FTP",
        "server": "127.0.0.1",
        "port": 8080,
        "usernane": "name",
        "password": "sample",
    }

    with open('app.ini', "w") as configFile:
        config.write(configFile)
