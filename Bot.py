from Scraper import Scraper
import discord
from discord.ext import commands
from utils import get_token
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
        super().__init__(command_prefix='%')
        self.scraper = Scraper()
        self.remove_command('help')
        self.loop.create_task(self.change_status())
        self.owner_id = 382152478810046464 # Jon
        self.server_id = 574641536214630401 # Pastries
        self.bot_channel = 574646616489721887 #bot-channel
        self.startup_extensions = ['Modules.General', 'Modules.Market', 'Modules.Boss']

    async def change_status(self):
        await self.wait_until_ready()
        while True:
            await self.change_presence(activity=discord.Activity(name='Pastries', type=3))
            await asyncio.sleep(10)
            await self.change_presence(activity=discord.Activity(name='use %help', type=1))
            await asyncio.sleep(10)

    def get_server_id(self):
        return self.server_id

    def get_owner_id(self):
        return self.owner_id

    def get_bot_channel(self):
        return self.bot_channel

    def run(self):
        for ext in self.startup_extensions:
            try:
                self.load_extension(ext)
            except Exception as e:
                print(f'An extension failed to run - {ext}: {e}')
        super().run(get_token(), reconnect=True)



