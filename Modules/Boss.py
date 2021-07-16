from discord.ext import commands
from utils import next_boss, time_diff
# from utils import next_boss
import asyncio, Constants
from discord.utils import get
from Logger import logger

"""
Boss class which is a derived class of Cogs
This class contains commands and listeners for anything related to world boss spawns.
Currently there is only a (un)set Boss Hunter role, next boss and boss reminder function
"""

class Boss(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.BOSS)
        self.bot = bot
        self.bot.loop.create_task(self.boss_reminder())

    @commands.command(name=Constants.BOSSHUNTER_L)
    async def set_bh_role(self, message):
        role = get(message.guild.roles, id=Constants.ID_ROLE_BOSSHUNTER)
        member = message.author
        chn = message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send(Constants.MSG_ROLE_REGISTER.format(message, Constants.BOSS_HUNTER))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send(Constants.MSG_ROLE_RESIGN.format(message, Constants.BOSS_HUNTER))

    @commands.command(name=Constants.WB_L)
    async def next_world_boss(self, chn):
        await chn.send(Constants.MSG_NEXT_BOSS_ANNC.format(next_boss().get_name(), next_boss().get_time().strftime(Constants.DT_FORMAT_WB)))

    @commands.Cog.listener()
    async def boss_reminder(self):
        await self.bot.wait_until_ready()
        chn = self.bot.get_channel(Constants.ID_CHN_BOT_CHN)

        for role in self.bot.get_guild(self.bot.get_server_id()).roles:
            if role.name == Constants.BOSS_HUNTER:
                bh = role
        while not self.bot.is_closed():
            if time_diff(next_boss().get_time()) == Constants.BOSS_NOTIFICATION_NOTICE_SECONDS:
                logger.info(Constants.BOSS_NOTIFICATION_SENT, next_boss().get_name())
                await chn.send(Constants.MSG_NEXT_BOSS_REMINDER.format(bh.mention, next_boss().get_name()))
            await asyncio.sleep(1)


def setup(bot):
    bot.add_cog(Boss(bot))
