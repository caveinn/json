import threading
import configparser
import os
from ftplib import FTP
# import pysftp
import json
import threading
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def get_config():
    config = configparser.ConfigParser()
    config.read("app.ini")
    return config

def write_config(config):
    with open('app.ini', "w") as configFile:
        config.write(configFile)

class Services():
    password = "@password1crealto"
    config = get_config()
    # def login_ftp(self):
    #     user = "marco@crealto.ch"
    #     password = "@password1crealto"

    #     with FTP("ftp.visuals.ch", "devapg@visualsplus.ch", password) as ftp:
    #         ftp.login()

    # def login_sftp(self):
    #     pass

    def is_file(self, filename, ftp):
        current = ftp.pwd()
        try:
            ftp.cwd(filename)
        except:
            ftp.cwd(current)
            return True
        ftp.cwd(current)
        return False

    def delete_remote(self, filename,):
        config = get_config()["INCOMING"]
        with FTP(config["server"], config["username"], config["password"]) as tempftp:
            tempftp.cwd(config["json_path"])
            tempftp.delete(filename)
            tempftp.quit()

    def upload_remote(self, filename):
        config = get_config()["DELIVERY"]
        with FTP(config["server"], config["username"], config["password"]) as ftp:
            ftp.cwd(config["delivery_path"])
            myfile = open(f"/Users/kevinnzioka/Desktop/test/ae/{filename}.mp4", "rb")
            ftp.storbinary(f"STOR {filename}.mp4", myfile)
            myfile.close()
            ftp.quit()

    def send_mail(self, firstname, lastname, filelink, expirydate, referenece, to_address):
        config = get_config()["EMAIL"]
        msg = MIMEMultipart()
        msg['From'] = config["adress"]
        msg['To'] = to_address
        msg['Subject'] = 'File Upload Successful'
        message = config["message"].replace("[FirstName]", firstname).replace("[LastName]", lastname).replace(
            "[FileLink]", filelink).replace("[ExpiryDate]", expirydate).replace("[Reference]", referenece)
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP(config["server"])
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login(config["username"], config["password"])
        a = mailserver.sendmail(config['adress'], to_address, msg.as_string())
        mailserver.quit()

    def save_files(self, files, ftp, parent):
        if get_config().getboolean("APP", "services_stopped"):
            return
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
        if get_config().getboolean("APP", "services_stopped"):
            return
        path = get_config()["ADS"]["campaign_json_path"]
        os.makedirs(path, exist_ok=True)
        config = get_config()
        with FTP(config["INCOMING"]["server"], config["INCOMING"]["username"], config["INCOMING"]["password"]) as ftp:
            ftp.cwd(config["INCOMING"]["json_path"])
            files = ftp.nlst()
            self.save_files(files, ftp, path)
            ftp.quit()

    def download_ads(self):
        save_dir = os.getcwd()
        save_dir = os.path.join(save_dir, "test")
        os.makedirs(save_dir, exist_ok=True)
        config = get_config()
        with FTP(config["INCOMING"]["server"], config["INCOMING"]["username"], config["INCOMING"]["password"]) as ftp:
            ftp.cwd(config["INCOMING"]["ads_path"])
            files = ftp.nlst()
            self.save_files(files, ftp, save_dir)
            print(f"working dir at start = {save_dir}")
            x = 1/0
            ftp.quit()

    def check_json(self):
        try:
            if not get_config().getboolean("APP", "services_stopped"):
                print(not get_config().getboolean("APP", "services_stopped"))
                name = get_config()["ADS"]["ae_file"]
                with open(name) as json_file:
                    data = json.load(json_file)
                    for entry in data:
                        if entry["render-status"] != "done":
                            time.sleep(2)
                            self.check_json()
                self.replace()
                self.check_json()
            else:
                return
        except Exception as e:
            config = get_config()
            config["ERRORS"]["json_error"] = config["ERRORS"]["json_error"] + "," + str(e)
            write_config(config)

    def get_json_data(self, json_file_path):
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            return_data = []
            for i in data:
                if i["render-status"] == "ready":
                    return_data.append(i)

            return return_data

    def replace(self):
        if not get_config().getboolean("APP", "services_stopped"):
            data = ''
            path = get_config()["ADS"]["campaign_json_path"]
            campaigns = os.listdir(path)
            campaign = ''
            processed = os.path.join(path, 'processing',)
            os.makedirs(processed, exist_ok=True)
            processed_files = os.listdir(processed)
            for f in processed_files:
                del_path = os.path.join(processed, f)
                # check if mp4 is created and send it to ftp
                json_data = self.get_json_data(del_path)
                for i in json_data:
                    video_file =os.path.join(get_config()["AE"]["render"], f"{i['output']}.mp4")
                    if os.path.isfile(video_file):
                        self.upload_remote(i['output'])
                        print("sending email")
                        # self.send_mail(i.get("user_firstname", ""),i.get("user_lastname", ""),"link",i.get("date"),i.get("reference", ""),i.get("email-delivery", ""))
                        self.send_mail(i.get("user_firstname", ""),i.get("user_lastname", ""),"link",i.get("date"),i.get("reference", ""),"caveinncicad@gmail.com")
                print(f"deleting {f}")
                f="to_delete.json"
                self.delete_remote(f)
                os.remove(del_path)
            curr_path = ''
            if campaigns:
                campaign = campaigns[0]
                curr_path = os.path.join(path, campaign)
            if campaign and os.path.isfile(curr_path) and not curr_path.endswith(".DS_Store"):
                with open(curr_path) as json_file:
                    data = json.load(json_file)
                proccessing_campaign_path = os.path.join(processed, campaign)
                os.rename(curr_path, proccessing_campaign_path)
            else:
                print("Downloading Json")
                self.download_json()
            path = self.config["ADS"]["campaign_json_path"]
            name = self.config["ADS"]["ae_file"]

            with open(name, "w") as json_file:
                json.dump(data, json_file)
        else:
            return

    def run_services(self):
        self.json_thread = threading.Thread(target=self.check_json)
        # thread2 = threading.Thread(target=self.test_shedule2)
        # thread2.start()
        self.json_thread.start()


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
        "server": "ftp.visualsplus.ch",
        "port": 21,
        "username": "devapg@visualsplus.ch",
        "password": "@password1crealto",
        "delivery_path": "delivery"
    }

    config["INCOMING"] = {
        "protocal": "FTP",
        "server": "ftp.visualsplus.ch",
        "port": 21,
        "username": "devapg@visualsplus.ch",
        "password": "@password1crealto",
        "json_path": "a/storage/private/Ads",
        "ads_path": "a/storage/private/json"
    }
    config["ERRORS"] ={
        "json_error": ""
    }

    with open('app.ini', "w") as configFile:
        config.write(configFile)
