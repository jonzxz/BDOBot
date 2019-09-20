from discord.ext import commands
from utils import next_boss, time_diff
import asyncio
from discord.utils import get

"""
Boss class which is a derived class of Cogs
This class contains commands and listeners for anything related to world boss spawns.
Currently there is only a (un)set Boss Hunter role, next boss and boss reminder function
"""

class Boss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.boss_reminder())

    @commands.command(name='bosshunter')
    async def set_bh_role(self, message):
        role = get(message.guild.roles, name='Boss Hunter')
        member = message.author
        chn = message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send("{0.author.mention} is now registered as a boss hunter!".format(message))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send("{0.author.mention} have resigned as a boss hunter!".format(message))

    @commands.command(name='wb')
    async def next_world_boss(self, chn):
        msg = ('The next boss is ' + next_boss().get_name() + ' at ' + next_boss().get_time().strftime('%H:%M') + 'hrs, GMT+8')
        await chn.send('```diff\n- ' + msg + '```')

    @commands.Cog.listener()
    async def boss_reminder(self):
        await self.bot.wait_until_ready()
        chn = self.bot.get_channel(self.bot.get_bot_channelid())

        for role in self.bot.get_guild(self.bot.get_server_id()).roles:
            if role.name == 'Boss Hunter':
                bh = role
        while not self.bot.is_closed():
            if time_diff(next_boss().get_time()) == 1800:
                await chn.send(bh.mention + '\n```md\n' + next_boss().get_name() + ' will spawn in 30 minutes time!```')
            await asyncio.sleep(1)


def setup(bot):
    bot.add_cog(Boss(bot))