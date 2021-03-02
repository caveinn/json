import threading
import configparser
import os
from ftplib import FTP
# import pysftp
import json
import threading
import time


def get_config():
    config = configparser.ConfigParser()
    config.read("app.ini")
    return config
class Services():
    password = "@password1crealto"
    config = get_config()
    def login_ftp(self):
        user = "marco@crealto.ch"
        password = "@password1crealto"

        with FTP("ftp.visuals.ch", "devapg@visualsplus.ch", password) as ftp:
            ftp.login()

    def login_sftp(self):
        pass

    def is_file(self, filename, ftp):
        current = ftp.pwd()
        try:
            ftp.cwd(filename)
        except:
            ftp.cwd(current)
            return True
        ftp.cwd(current)
        return False

    def save_files(self, files, ftp, parent):
        for file in files:
            if self.is_file(file, ftp):
                local_file = os.path.join(parent, file)
                print(f"saving{local_file}")
                new_file = open(local_file, 'wb+')
                ftp.retrbinary("RETR "+file, new_file.write)
            elif file != "." and file != "..":
                new_parent = os.path.join(parent, file)
                os.makedirs(new_parent, exist_ok=True)
                ftp.cwd(file)
                new_files = ftp.nlst()
                print(f"new dir= {parent}")
                self.save_files(new_files, ftp, new_parent)
                ftp.cwd("..")

    def download_json(self):
        path = self.config["ADS"]["campaign_json_path"]
        os.makedirs(path, exist_ok=True)
        with FTP("ftp.visualsplus.ch", "devapg@visualsplus.ch", self.password) as ftp:
            ftp.cwd("a/storage/private/json")
            files = ftp.nlst()
            self.save_files(files, ftp, path)
            ftp.quit()

    def download_ads(self):
        save_dir = os.getcwd()
        save_dir = os.path.join(save_dir, "test")
        os.makedirs(save_dir, exist_ok=True)
        with FTP("ftp.visualsplus.ch", "devapg@visualsplus.ch", self.password) as ftp:
            ftp.cwd("a/storage/private/Ads")
            files = ftp.nlst()
            self.save_files(files, ftp, save_dir)
            print(f"working dir at start = {save_dir}")
            ftp.quit()

    def check_json(self):
        name = self.config["ADS"]["ae_file"]
        with open(name) as json_file:
            data = json.load(json_file)
            for entry in data:
                if entry["render-status"] != "done":
                    time.sleep(2)
                    self.check_json()
        self.replace()
        self.check_json()

    def replace(self):
            data = ''
            path = self.config["ADS"]["campaign_json_path"]
            campaigns = os.listdir(path)
            campaign = ''
            processed= os.path.join(path, 'processing',)
            os.makedirs(processed, exist_ok=True)
            processed_files = os.listdir(processed)
            for f in processed_files:
                del_path = os.path.join(processed, f)
                os.remove(del_path)
            curr_path = ''
            if campaigns:
                campaign = campaigns[0]
                curr_path = os.path.join(path, campaign)
                print(curr_path)
            if campaign and  os.path.isfile(curr_path):
                with open(curr_path) as json_file:
                    data = json.load(json_file)
                proccessing_campaign_path = os.path.join(processed,campaign)
                os.rename(curr_path, proccessing_campaign_path)
            else:
                print("Downloading Json")
                self.download_json()
            path = self.config["ADS"]["campaign_json_path"]
            name = self.config["ADS"]["ae_file"]

            with open(name, "w") as json_file:
                json.dump(data, json_file)


    def run_services(self):
        thread1 = threading.Thread(target=self.check_json)
        # thread2 = threading.Thread(target=self.test_shedule2)
        # thread2.start()
        thread1.start()





def is_image(path):
    if path.lower().endswith((".png", ".jpg", ".jpeg")):
        return True
    return False


def init_config_file():
    if os.path.exists("app.ini"):
        return
    config = configparser.ConfigParser()
    config['APP'] = {
        "logo": '',
        "lastCampaign_code": "000808",
        "lastCampaign_date": "randomDate",
        "syncJson": "01.11.2020@10:25am",
        "automaticallyStart": False,
        "services_stopped": True,
        "sync_folder": "01.11.2020@10:25am"
    }
    config['GENERAL'] = {
        "online_availability_duration": 1,
        "master_availability_duration": 1,
        "sync_interval": 5,
    }
    config["ADS"] = {
        "campaign_JSON_path": "~/Desktop/campaign",
        "AE_file": "~/Desktop/AEjson",
        "ADs": "~/Desktop/ads"
    }

    config["EMAIL"] = {
        "message": '''
 Dear[fisrt name][last name]

 Your file to the campaign [reference] is available for download at [file link]

 The link wil expire on [expiry date]

 Best Regars, your APGS|SGA Ad eMotion Team
        ''',
        "adress": "example@example.com",
        "server": "127.0.0.1",
        "port": "8080",
        "username": "example",
        "password": "sample"
    }

    config["AE"] = {
        "project": "path here",
        "render": "path here",
        "backup_path": " path here",
    }
    config["DELIVERY"] = {
        "protocal": "FTP",
        "server": "127.0.0.1",
        "port": 8080,
        "usernane": "name",
        "password": "sample",
        "delivery_path": "path_here"
    }

    config["INCOMING"] = {
        "protocal": "FTP",
        "server": "127.0.0.1",
        "port": 8080,
        "usernane": "name",
        "password": "sample",
    }

    with open('app.ini', "w") as configFile:
        config.write(configFile)
