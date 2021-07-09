from pyrogram import Client, __version__
from pyromod import listen
from Bot.config import APP_ID, API_HASH, TG_BOT_WORKERS, TG_BOT_TOKEN, LOGGER

class Bot(Client):
    def __init__(self):
        plugins = dict(root="Bot/plugins")
        super().__init__(
            "CodeXBotz",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins=plugins,
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.username = '@' + usr_bot_me.username
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started!\n\n"
        )
        self.me = usr_bot_me

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")