from discord.ext import commands
import math, Constants
from Logger import logger

"""
Market class that extends commands.Cog - this class currently only has a single %mp function
that calculates the profit earned with(out) Value Pack
"""

class Market(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.MARKET)
        self.bot = bot

    @commands.command(name=Constants.MARKETPLACE_L)
    async def check_profit(self, ctx, silver):
        await ctx.send('```fix\n' + (self.mp_check(silver) + '```'))

    # Function that returns a string message describing the profit
    def mp_check(self, silver):
        return 'Without VP : ' + str(math.floor(float(silver) * 0.65)) + '\nWith VP\t: '\
               + str(math.floor(float(silver) * 0.845)) + '\nValues might be a little off depending on your family fame!'


def setup(bot):
    bot.add_cog(Market(bot))
