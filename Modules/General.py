from discord.ext import commands
import discord, asyncio
import re, emoji
from Logger import logger
from discord.utils import get
"""
General class that is a derived class of commands.Cog
This class contains most of the bots commands and listeners.
Some of these commands will probably be shifted to another Cog when more features are implemented
"""


class General(commands.Cog):
    def __init__(self, bot):
        logger.info("starting up General Cog")
        self.bot = bot
        self.react_chosen = None

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Starting up bot with ID: %s, Name: %s", self.bot.user.id, self.bot.user.name)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logger.info("someone has left the server, sending notice..")
        ctx = member.guild.system_channel
        if ctx is not None:
            await ctx.send("{0} has left the server.".format(member.display_name))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logger.info("someone new has joined, sleeping for 25s before sending welcome")
        ctx = member.guild.system_channel
        await asyncio.sleep(25)
        if ctx is not None:
            if self.bot.get_recruit_open() == True or self.bot.get_recruit_open() == None:
                about_us = self.bot.get_channel(575282309947850822)
                await ctx.send(file=discord.File('assets/poster.png'))
                await ctx.send(':sparkles::pretzel:**Hello fresh dough {0.mention}, welcome to Pastries!**:sparkles::pretzel:\n'
                               'We would like you to answer the following short questions before proceeding!\n\n'
                               '> **01. What are you looking for in a guild?** *i.e. Payouts, socializing, guidance in game*\n\n'
                               '> **02. Have you been in a guild before?** *If YES, what guild and why did you leave?*\n\n'
                               '> **03. What kind of player do you consider yourself as?** *PVE, PVP, Lifeskill-oriented, or an all-rounded?*\n\n'
                               '> **04. OPTIONAL - What is your nationality?** *We got people from MY/SG/INA/PH and a few more other countries inside!*\n\n'
                               ':cake:By answering these questions, you also acknowledge that **Pastries is a chill International PVX/Lifeskill guild**\n'
                               ':cake:**We do not tolerate any form of unhealthy or immature behaviours when you are with us!**\n'
                               ':cake:Please head over to {1.mention} for more info and our guild rules!\n\n'
                               '**Thank you for answering the questions - Please mention Crème brûlée when you are done**\n'
                               '*We look forward to get to know you better!*\n\n'.format(member, about_us))
            else:
                await ctx.send(':pretzel:**Welcome to Pastries!**:pretzel:\n\n' \
                                'Hello {0.mention}, Thank you for visiting our discord!\n' \
                                'We\'d really love to have you joining our little bakery.\nBut unfortunately, ' \
                                ':no_entry_sign:**our recruitment is CLOSED**:no_entry_sign: for the time being!\n' \
                                'Hopefully we\'d meet again in the next chance!\n\nIf you have any questions ' \
                                'feel free to mention Crème brûlée!\n' \
                                '*While you\'re here, please have some free cheese garlic bread* :sparkles:\n'.format(member), file=discord.File('assets/garlic_bread.png'))
    @commands.command(name='help')
    async def help_info(self, ctx):
        content = str("```yaml\n" \
                  "List of Commands\n----------------\n\n" \
                  "%help - shows this message\n\n" \
                  "%foodname - retrieves ingredients i.e. %5 beer\n\n" \
                  "%wb - shows the upcoming world boss\n\n" \
                  "%bosshunter - (un)register the Boss Hunter role.\n\n" \
                  "Receive notifications 30 minutes before world boss!\n\n" \
                  "%popcorn - (un)register the Caramel Popcorn role.\n\n" \
                  "%mp - shows profit with(out) VP from selling in MP i.e. %mp 43500000\n\n" \
                  "%hystria - sends a map of hystria!\n\n" \
                  "%meme - sends a random meme\n\n" \
                  "%calc - built-in calculator, supports +, -, *, /, %\n\n" \
                  "%anime <title> - retrieves anime information from MyAnimeList\n\n" \
                  "%manga <title> - retrieves manga information from MyAnimeList\n\n" \
                  "%recruit - Update recruitment status (Crème brûlées only!)\n\n" \
                  "%khan - Update Khan announcement status (Crème brûlées only!)\n\n" \
                  "%war - Update Node War announcement status (Crème brûlées only!)\n\n" \
                  "%bug <message> - reports a bug to Kagi\n\n```")
        await ctx.send(content)

    @commands.command(name='bug')
    async def bug(self, ctx):
        await ctx.send('<@!{}> A bug have been discovered!'.format(self.bot.get_owner_id()))

    @commands.command(name='hystria')
    async def send_hyst_map(self, ctx):
        await ctx.send(file=discord.File('assets/hystria.png'))

    @commands.command(name='sycraia')
    async def send_hyst_map(self, ctx):
        await ctx.send(file=discord.File('assets/sycraia.png'))

    @commands.command(name='calc')
    async def calculate(self, ctx, msg):
        try:
            await ctx.send('```{0} is {1}```'.format(msg, str(eval(msg))))
        except SyntaxError:
            await ctx.send('```Sorry, I didn\'t get that, please use +, -, *, /, % only!```')

    # @commands.command(name='whalecome')
    # async def test_feature(self, ctx):
    #     await ctx.send(':sparkles::pretzel:**Hello fresh dough {0}, welcome to Pastries!**:sparkles::pretzel:\n'
    #                    'We would like you to answer the following short questions before proceeding!\n\n'
    #                    '> **01. What are you looking for in a guild?** *i.e. Payouts, socializing, guidance in game*\n\n'
    #                    '> **02. Have you been in a guild before?** *If YES, what guild and why did you leave?*\n\n'
    #                    '> **03. What kind of player do you consider yourself as?** *PVE, PVP, Lifeskill-oriented, or an all-rounded?*\n\n'
    #                    '> **04. OPTIONAL - What is your nationality?** *We got people from MY/SG/INA/PH and a few more other countries inside!*\n\n'
    #                    ':cake:By answering these questions, you also acknowledge that **Pastries is a chill International PVX/Lifeskill guild**\n'
    #                    ':cake:**We do not tolerate any form of unhealthy or immature behaviours when you are with us!**\n'
    #                    ':cake:Please head over to #about-us for more info and our guild rules!\n\n'
    #                    '**Thank you for answering the questions - Please mention Crème brûlée when you are done**\n'
    #                    '*We look forward to get to know you better!*\n\n'.format("kagi"), file=discord.File('assets/poster.png'))


    @commands.command(name='recruit')
    async def recruit(self, message):
        author_roles = message.author.roles
        chn = message.channel
        self.react_chosen = None

        if self.bot.get_officer_id() in [role.id for role in author_roles]:
            status_emoji = '\U0001f35e'
            open_emoji = '\U00002b55'
            close_emoji = '\U0000274c'
            msg = await chn.send('Please react to enquire or update recruitment status!\n\n' \
                            ':bread: - Recruitment Status\n\n:o: - Opening of recruitment \n\n:x: - Closing of recruitment')
            await msg.add_reaction(status_emoji)
            await msg.add_reaction(open_emoji)
            await msg.add_reaction(close_emoji)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == status_emoji:
                        logger.info("%s status triggered", user)
                        self.react_chosen = "STATUS"
                    if reaction.emoji == open_emoji:
                        logger.info("open recruitment triggered")
                        self.react_chosen = "OPEN"
                        self.bot.set_recruit_open(True)
                    if reaction.emoji == close_emoji:
                        logger.info("close recruitment triggered")
                        self.react_chosen = "CLOSE"
                        self.bot.set_recruit_open(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=7, check=check)
                await msg.delete()
                logger.info("REACT_CHOSEN %s", self.react_chosen)
                if self.react_chosen == "OPEN" or self.react_chosen == "CLOSE":
                    if self.bot.get_recruit_open():
                        await chn.send("{0.mention} ```Updated recruitment status to open!```".format(message.author))
                    if not self.bot.get_recruit_open():
                        await chn.send("{0.mention} ```Updated recruitment status to closed!```".format(message.author))
                else:
                    await chn.send("```Recruitment Status: {0}```".format("OPEN" if self.bot.get_recruit_open() else "CLOSED"))
            except asyncio.TimeoutError:
                logger.info("hit timeout, removing message")
                await msg.delete()
        else:
            await chn.send("```Only Crème brûlées are allowed to use this feature!```")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error

    @commands.Cog.listener()
    async def on_message(self, msg):
        BAKERY_ID = 574641537548550156
        if msg.author != self.bot.user:
            channel = msg.channel
            content = msg.content.lower()
            ctx = await self.bot.get_context(msg)
            if 'hello' in content:
                await channel.send('Hello {0.mention}!'.format(msg.author))
            if 'nezuko' in content:
                await channel.send(file=discord.File('assets/nezuko.gif'))
            if 'twitch.tv' in content and channel.id == BAKERY_ID:
                await channel.send('Hello {0.mention}, it seems like you have pasted a Twitch link. All videos or stream advertisements goes to #media, thank you!'.format(msg.author))
                await msg.delete()
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
