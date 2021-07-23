from discord.ext import commands
import discord, asyncio, re, emoji, Constants
from Logger import logger
from discord.utils import get
"""
General class that is a derived class of commands.Cog
This class contains most of the bots commands and listeners.
Some of these commands will probably be shifted to another Cog when more features are implemented
"""


class General(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.GENERAL)
        self.bot = bot
        self.react_chosen = None

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(Constants.BOT_STARTUP, self.bot.user.id, self.bot.user.name)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logger.info(Constants.ON_MEMBER_REMOVE, member.display_name)
        entry_chn = self.bot.get_channel(Constants.ID_CHN_ENTRY)
        if entry_chn:
            await entry_chn.send(Constants.MSG_ON_MEMBER_REMOVE.format(member.display_name))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logger.info(Constants.ON_MEMBER_JOIN, member.display_name)
        entry_chn = self.bot.get_channel(Constants.ID_CHN_ENTRY)
        await asyncio.sleep(25)
        if entry_chn:
            if self.bot.get_recruit_open():
                about_us = self.bot.get_channel(Constants.ID_CHN_ABOUT_US)
                await entry_chn.send(file=discord.File(Constants.ASSET_POSTER))
                await entry_chn.send(Constants.MSG_REC_OPEN_MSG.format(member, about_us))
            else:
                await entry_chn.send(MSG_REC_CLOSED_MSG.format(member), file=discord.File(Constants.ASSET_REC_CLOSE))

    @commands.command(name=Constants.HELP_L)
    async def help_info(self, chn):
        help_msg = str(Constants.MSG_HELP_MSG)
        await chn.send(help_msg)

    @commands.command(name=Constants.BUG_L)
    async def bug(self, chn):
        await chn.send(Constants.MSG_BUG_DISCOVERED.format(self.bot.get_owner_id()))

    @commands.command(name=Constants.HYSTRIA_L)
    async def send_hyst_map(self, chn):
        await chn.send(file=discord.File(Constants.ASSET_HYSTRIA))

    @commands.command(name=Constants.SYCRAIA_L)
    async def send_syc_map(self, chn):
        await chn.send(file=discord.File(Constants.ASSET_SYCRAIA))

    @commands.command(name=Constants.CALC_L)
    async def calculate(self, chn, msg):
        try:
            await chn.send(Constants.MSG_CALC_RES.format(msg, str(eval(msg))))
        except SyntaxError:
            await chn.send(Constants.MSG_CALC_FAIL)

    @commands.command(name=Constants.RECRUIT_L)
    async def recruit(self, message):
        chn = message.channel
        self.react_chosen = None

        if Constants.ID_ROLE_CREME in [role.id for role in message.author.roles]:
            status_emoji = Constants.EMOJI_STATUS
            open_emoji = Constants.EMOJI_OPEN
            close_emoji = Constants.EMOJI_CLOSE
            msg = await chn.send(Constants.MSG_RECRUIT_ENQUIRY)
            await msg.add_reaction(status_emoji)
            await msg.add_reaction(open_emoji)
            await msg.add_reaction(close_emoji)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == status_emoji:
                        logger.info(Constants.RECRUIT_TRIGGER, Constants.STATUS, user.display_name)
                        self.react_chosen = Constants.STATUS
                    if reaction.emoji == open_emoji:
                        logger.info(Constants.RECRUIT_TRIGGER, Constants.STATUS, user.display_name)
                        self.react_chosen = Constants.OPEN
                        self.bot.set_recruit_open(True)
                    if reaction.emoji == close_emoji:
                        logger.info(Constants.RECRUIT_TRIGGER, Constants.CLOSE, user.display_name)
                        self.react_chosen = Constants.CLOSE
                        self.bot.set_recruit_open(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for(Constants.REACTION_ADD, timeout=Constants.REACTION_TIMEOUT_SECONDS, check=check)
                await msg.delete()
                logger.info(Constants.REACTION_CHOSEN, self.react_chosen)
                if self.react_chosen == Constants.OPEN or self.react_chosen == Constants.CLOSE:
                    if self.bot.get_recruit_open():
                        await chn.send(MSG_RECRUIT_OPEN_UPDATE.format(message.author))
                    if not self.bot.get_recruit_open():
                        await chn.send(MSG_RECRUIT_CLOSE_UPDATE.format(message.author))
                else:
                    await chn.send(Constants.MSG_RECRUIT_STATUS.format(Constants.OPEN if self.bot.get_recruit_open() else Constants.CLOSE))
            except asyncio.TimeoutError:
                logger.info(Constants.REACT_TIMEOUT, Constants.RECRUIT)
                await msg.delete()
        else:
            await chn.send(Constants.MSG_COMD_DENIED)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author != self.bot.user:
            chn = msg.channel
            content = msg.content.lower()
            ctx = await self.bot.get_context(msg)
            if Constants.HELLO_L in content:
                await chn.send(Constants.MSG_HELLO_MENTION.format(msg.author))
            if Constants.NEZUKO_L in content:
                await chn.send(file=discord.File(Constants.ASSET_NEZUKO))
            if Constants.TWITCHTV_L in content and chn.id == Constants.ID_CHN_BAKERY:
                await chn.send(Constants.MSG_TWITCH_WARNING.format(msg.author, self.bot.get_channel(Constants.ID_CHN_MEDIA)))
                await msg.delete()
            elif content.startswith(Constants.PREFIX_PERCENT) and ctx.valid is False:
                results = self.bot.get_scraper().print_ingredients(content)
                if not results:
                    reply = Constants.MSG_INVALID_COMD
                else:
                    reply = Constants.NEW_LINE.join(results)
                await chn.send('```' + reply + '```')
        else:
            return

def setup(bot):
    bot.add_cog(General(bot))
