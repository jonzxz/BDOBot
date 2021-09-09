import discord, asyncio, Constants
from Logger import logger
from discord.ext import commands

class Development(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, 'Development')
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(Constants.BOT_STARTUP, self.bot.user.id, self.bot.user.name)

    @commands.command(name='gunir')
    async def help_info(self, chn):
        help_msg = str(Constants.MSG_HELP_MSG)
        await chn.send(help_msg)

def setup(bot):
    bot.add_cog(Development(bot))