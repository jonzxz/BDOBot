import discord, asyncio, Constants
from Logger import logger
from discord.ext import commands
from discord_components import *
from utils import add_msg_reactions
import pendulum
from datetime import datetime
from discord import File, User
from utils import is_brioche_bun
from discord.errors import NotFound

class Development(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, 'Development')
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(Constants.BOT_STARTUP, self.bot.user.id, self.bot.user.name)

    @commands.command(name=Constants.INTRO_L)
    async def send_intro_qn(self, ctx, msg):
        if is_brioche_bun(ctx.message.author.roles):
            about_us = self.bot.get_channel(Constants.ID_CHN_ABOUT_US)
            try:
                member = await self.bot.fetch_user(msg[3:-1])
                logger.info("{0} invoked intro for {1}".format(ctx.message.author.display_name, member.display_name))
            except NotFound:
                logger.info("Unknown user fetched by {0}, setting member to empty string and sending generic welcome message instead".format(ctx.message.author.display_name))
                member = None
            finally:
                await ctx.message.delete()
                await ctx.send(file=discord.File(Constants.ASSET_POSTER))
                await ctx.send(Constants.MSG_REC_OPEN_MSG.format(member.mention, about_us)) \
                if member else await ctx.send(Constants.MSG_REC_OPEN_MSG.format('', about_us))


def setup(bot):
    bot.add_cog(Development(bot))