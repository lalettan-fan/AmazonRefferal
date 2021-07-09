from os import environ

class Config(object):
    API_ID = int(environ.get("API_ID", None))
    API_HASH = environ.get("API_HASH", None)
    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    BOT_WORKERS = environ.get("BOT_WORKERS", "4")
    AUTH_CHANNEL1 = environ.get("AUTH_CHANNEL1",None)
    AUTH_CHANNEL2 = environ.get("AUTH_CHANNEL2", None)
    SUDO_USERS = environ.get("SUDO_USERS",None)
    NO_OF_REFFERAL = environ.get("NO_OF_REFFERAL",15)
    DB_URI = environ.get("DATABASE_URL",None)