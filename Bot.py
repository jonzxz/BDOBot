from Scraper import Scraper
import discord, asyncio, Constants
from discord.ext import commands
from utils import get_token
from datetime import datetime
from Logger import logger

"""
Bot class that extends commands.Bot
This class is the main class of the program.
"""

class BDOBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=Constants.PREFIX_PERCENT, intents=self.init_intents())
        self.__scraper = Scraper()
        self.remove_command(Constants.HELP_L)
        self.loop.create_task(self.change_status())

        self.__owner_id = Constants.ID_USER_KAGI
        self.__server_id = Constants.ID_SERVER_PASTRIES
        self.__is_recruit_open = True
        self.__is_khan_active = True
        self.__is_war_active = True
        self.__next_khan_annc = None
        self.__next_war_annc = None

        self.startup_extensions = Constants.STARTUP_COG_MODULES

    async def change_status(self):
        await self.wait_until_ready()
        while True:
            await self.change_presence(activity=discord.Activity(name=Constants.PASTRIES, type=3))
            await asyncio.sleep(Constants.STATUS_LOOP_TIME_SECONDS)
            await self.change_presence(activity=discord.Activity(name=Constants.STATUS_MSG_USE_HELP, type=1))
            await asyncio.sleep(Constants.STATUS_LOOP_TIME_SECONDS)

    def get_server_id(self) -> int:
        return self.__server_id

    def get_owner_id(self) -> int:
        return self.__owner_id

    def get_scraper(self) -> Scraper:
        return self.__scraper

    def get_recruit_open(self) -> bool:
        return self.__is_recruit_open

    def set_recruit_open(self, bool: bool) -> None:
        self.__is_recruit_open = bool

    def get_khan_active(self) -> bool:
        return self.__is_khan_active

    def set_khan_active(self, bool: bool) -> None:
        self.__is_khan_active = bool

    def get_war_active(self) -> bool:
        return self.__is_war_active

    def set_war_active(self, bool: bool) -> None:
        self.__is_war_active = bool

    def get_next_khan_annc(self) -> datetime:
        return self.__next_khan_annc

    def set_next_khan_annc(self, dt: datetime) -> None:
        self.__next_khan_annc = dt

    def get_next_war_annc(self) -> datetime:
        return self.__next_war_annc

    def set_next_war_annc(self, dt: datetime) -> None:
        self.__next_war_annc = dt

    def run(self) -> None:
        for ext in self.startup_extensions:
            try:
                self.load_extension(ext)
            except Exception as e:
                logger.error(Constants.EXT_FAILED_TO_RUN, ext, e)
        super().run(get_token(), reconnect=True)

    def init_intents(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        intents.reactions = True
        return intents
