import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfigfile:

    @staticmethod
    def GetUsername():
        username = config.get('Login data', 'username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('Login data', 'password')
        return password
