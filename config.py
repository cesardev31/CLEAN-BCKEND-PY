from decouple import config as decouple_config 

class Confing:
    SECRET_KEY = decouple_config("SECRET_KEY")


class DevelopmentConfig(Confing):
    DEBUG = True


config = {"development": DevelopmentConfig}
