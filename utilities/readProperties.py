# 2021 Dec 5 - customLogger.py
#
# Read "common info" that will be used by each test setup. Organized this way so that when the URL, username, password, etc
# change, it can be eddited in one location and passed to each test case instead of editing each test case. This is not for
# Data Driven Test method inputs.
#
import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password