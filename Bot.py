from Scraper import Scraper
import discord
from discord.ext import commands
from utils import get_token, get_global_configs, get_startup_modules
import asyncio

"""
Bot class that extends commands.Bot
This class is the main class of the program.
Information such as owner_id, server_id and bot_channel are all set here, as well as the cogs for this bot.
Ideally the id information should be stored in a global I think, and I can probably cleanup some of the code
here so that the bot can work anywhere outside from the current server_id server.
"""

class BDOBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='%', intents=self.init_intents())
        self.__scraper = Scraper()
        self.remove_command('help')
        self.loop.create_task(self.change_status())

        GLOBAL_CONFIGS = get_global_configs()
        self.__owner_id = GLOBAL_CONFIGS[0]
        self.__server_id = GLOBAL_CONFIGS[1]
        self.__is_recruit_open = True
        self.__is_khan_active = True
        self.__is_war_active = True
        self.__next_khan_annc = None
        self.__next_war_annc = None

        self.__OFFICER_ID = 574641817505497106
        self.__bot_channelid = 574646616489721887 #bot-channel
        self.__menu_channelid = 574650178183626771 #menu-board
        self.startup_extensions = get_startup_modules()

    async def change_status(self):
        await self.wait_until_ready()
        while True:
            await self.change_presence(activity=discord.Activity(name='Pastries', type=3))
            await asyncio.sleep(20)
            await self.change_presence(activity=discord.Activity(name='use %help', type=1))
            await asyncio.sleep(20)

    def get_server_id(self):
        return self.__server_id

    def get_owner_id(self):
        return self.__owner_id

    def get_bot_channelid(self):
        return self.__bot_channelid

    def get_menu_channelid(self):
        return self.__menu_channelid

    def get_scraper(self):
        return self.__scraper

    def get_recruit_open(self):
        return self.__is_recruit_open

    def set_recruit_open(self, bool):
        self.__is_recruit_open = bool

    def get_khan_active(self):
        return self.__is_khan_active

    def set_khan_active(self, bool):
        self.__is_khan_active = bool

    def get_war_active(self):
        return self.__is_war_active

    def set_war_active(self, bool):
        self.__is_war_active = bool

    def get_next_khan_annc(self):
        return self.__next_khan_annc

    def set_next_khan_annc(self, dt):
        self.__next_khan_annc = dt

    def get_next_war_annc(self):
        return self.__next_war_annc

    def set_next_war_annc(self, dt):
        self.__next_war_annc = dt

    def get_officer_id(self):
        return self.__OFFICER_ID

    def run(self):
        for ext in self.startup_extensions:
            try:
                self.load_extension(ext)
            except Exception as e:
                print(f'An extension failed to run - {ext}: {e}')
        super().run(get_token(), reconnect=True)

    def init_intents(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.reactions = True
        return intents
