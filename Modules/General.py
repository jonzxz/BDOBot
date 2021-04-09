from discord.ext import commands
import discord, asyncio
import re
from Logger import logger

"""
General class that is a derived class of commands.Cog
This class contains most of the bots commands and listeners.
Some of these commands will probably be shifted to another Cog when more features are implemented
"""


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Starting up bot with ID: %s, Name: %s", self.bot.user.id, self.bot.user.name)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logger.info("someone new has joined, sleeping for 25s before sending welcome")
        ctx = member.guild.system_channel
        await asyncio.sleep(25)
        if ctx is not None:
            await ctx.send('Hello fresh dough {0.mention}, welcome to Pastries!\n'
                           'We would like you to answer the following short questions before proceeding!\n\n'
                           '01. What are you looking for in a guild? i.e. Payouts, socializing, guidance in game\n\n'
                           '02. Have you been in a guild before? If YES, what guild and why did you leave?\n\n'
                           '03. What kind of player do you consider yourself as? PVE, PVP, Lifeskill-oriented, or well-balanced?\n\n'
                           '04. OPTIONAL - What is your nationality?\n\n'
                           'By answering these questions, you also acknowledge that Pastries is a chill international PVE/'
                           'Lifeskill guild, we do not tolerate any form of unhealthy or immature behaviours when you are with us!\n\n'
                           'Thank you for answering the questions - Please mention Crème brûlée when you are done\n'
                           'Meanwhile, head over to #rules to read our guild rules.\n'
                           'We look forward to get to know you better!\n\n'.format(member))

    @commands.command(name='help')
    async def help_info(self, ctx):
        content = str("```yaml\n" \
                  "List of Commands\n----------------\n\n" \
                  "%help - shows this message\n\n" \
                  "%foodname - retrieves ingredients i.e. %5 beer\n\n" \
                  "%wb - shows the upcoming world boss\n\n" \
                  "%bosshunter - (un)register the Boss Hunter role. "
                  "Receive notifications 30 minutes before world boss!\n\n" \
                  "%mp - shows profit with(out) VP from selling in MP i.e. %mp 43500000\n\n" \
                  "%hystria - sends a map of hystria!\n\n" \
                  "%meme - sends a random meme\n\n" \
                  "%calc - built-in calculator, supports +, -, *, /, %\n\n" \
                  "%anime <title> - sends anime details\n\n" \
                  "%bug <message> - reports a bug to Kagi\n\n```")
        await ctx.send(content)

    @commands.command(name='bug')
    async def bug(self, ctx):
        await ctx.send('<@!{}> A bug have been discovered!'.format(self.bot.get_owner_id()))

    @commands.command(name='hystria')
    async def send_hyst_map(self, ctx):
        await ctx.send(file=discord.File('assets/hystria.png'))

    @commands.command(name='calc')
    async def calculate(self, ctx, msg):
        try:
            await ctx.send('```{0} is {1}```'.format(msg, str(eval(msg))))
        except SyntaxError:
            await ctx.send('```Sorry, I didn\'t get that, please use +, -, *, /, % only!```')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author != self.bot.user:
            channel = msg.channel
            content = msg.content.lower()
            ctx = await self.bot.get_context(msg)
            if 'hello' in content:
                await channel.send('Hello {0.mention}!'.format(msg.author))
            if 'nezuko' in content:
                await channel.send(file=discord.File('assets/nezuko.gif'))
            elif content.startswith('%') and ctx.valid is False:
                results = self.bot.get_scraper().print_ingredients(content)
                if not results:
                    reply = "No results or commands was retrieved." \
                            "\nPerhaps you wanna use '%help'?"
                else:
                    reply = '\n'.join(results)
                await channel.send('```' + reply + '```')
            # await self.bot.process_commands(msg)
        else:
            return



def setup(bot):
    bot.add_cog(General(bot))
