import os
import logging
from logging.handlers import RotatingFileHandler

ENV = os.environ.get("ENV", False)

if ENV:
    from BotConfig import Config
else:
    from local_config import Development as Config


APP_ID = int(Config.API_ID)
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.BOT_TOKEN
TG_BOT_WORKERS = int(Config.BOT_WORKERS)
AUTH_CHANNEL1 = Config.AUTH_CHANNEL1
AUTH_CHANNEL2 = Config.AUTH_CHANNEL2
SUDO = Config.SUDO_USERS
NO_OF_REFFERAL = Config.NO_OF_REFFERAL
DB_URI = Config.DB_URI

LOG_FILE_NAME = "pyrogrambot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)