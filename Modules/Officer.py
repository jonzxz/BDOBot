from utils import add_msg_reactions, is_creme_brulee, is_brioche_bun
from discord.ext import commands
import Constants
from Logger import logger
from discord.utils import get
import discord, asyncio, re, emoji, csv
from discord.errors import NotFound

class Officer(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.OFFICER)
        self.bot = bot
        self.__recruit_react_chosen = None
        self.__khan_react_chosen = None
        self.__war_react_chosen_chosen = None

    @commands.command(name=Constants.RECRUIT_L)
    async def toggle_recruit(self, message):
        chn = message.channel
        self.recruit_react_chosen = None

        if is_creme_brulee(message.author.roles):
            msg = await chn.send(Constants.MSG_RECRUIT_ENQUIRY)
            await add_msg_reactions(msg, Constants.UPDATE)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == Constants.EMOJI_STATUS:
                        logger.info(Constants.RECRUIT_TRIGGER, Constants.STATUS, user.display_name)
                        self.set_recruit_react_chosen(Constants.STATUS)
                    if reaction.emoji == Constants.EMOJI_OPEN:
                        logger.info(Constants.RECRUIT_TRIGGER, Constants.STATUS, user.display_name)
                        self.set_recruit_react_chosen(Constants.OPEN)
                        self.bot.set_recruit_open(True)
                    if reaction.emoji == Constants.EMOJI_CLOSE:
                        logger.info(Constants.RECRUIT_TRIGGER, Constants.CLOSE, user.display_name)
                        self.set_recruit_react_chosen(Constants.CLOSE)
                        self.bot.set_recruit_open(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for(Constants.REACTION_ADD, timeout=Constants.REACTION_TIMEOUT_SECONDS, check=check)
                await msg.delete()
                logger.info(Constants.REACTION_CHOSEN, self.get_recruit_react_chosen())
                if self.get_recruit_react_chosen() and not self.get_recruit_react_chosen() == Constants.STATUS:
                    await chn.send(Constants.MSG_RECRUIT_OPEN_UPDATE.format(message.author) if self.bot.get_recruit_open() else Constants.MSG_RECRUIT_CLOSE_UPDATE.format(message.author))
                else:
                    await chn.send(Constants.MSG_RECRUIT_STATUS.format(Constants.OPEN if self.bot.get_recruit_open() else Constants.CLOSE))
            except asyncio.TimeoutError:
                logger.info(Constants.REACT_TIMEOUT, Constants.RECRUIT)
                await msg.delete()
        else:
            await chn.send(Constants.MSG_COMD_DENIED)
    
    @commands.command(name=Constants.KHAN_L)
    async def toggle_khan(self, message):
        chn = message.channel

        if is_creme_brulee(message.author.roles):
            msg = await chn.send(Constants.MSG_KHAN_ENQUIRY)
            await add_msg_reactions(msg, Constants.UPDATE)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == Constants.EMOJI_STATUS:
                        logger.info(Constants.KHAN_TRIGGER, Constants.STATUS, user.display_name)
                        self.set_khan_react_chosen(Constants.STATUS)
                    if reaction.emoji == Constants.EMOJI_OPEN:
                        logger.info(Constants.KHAN_TRIGGER, Constants.OPEN, user.display_name)
                        self.set_khan_react_chosen(Constants.OPEN)
                        self.bot.set_khan_active(True)
                    if reaction.emoji == Constants.EMOJI_CLOSE:
                        logger.info(Constants.KHAN_TRIGGER, Constants.CLOSE, user.display_name)
                        self.set_khan_react_chosen(Constants.CLOSE)
                        self.bot.set_khan_active(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for(Constants.REACTION_ADD, timeout=Constants.REACTION_TIMEOUT_SECONDS, check=check)
                await msg.delete()
                logger.info(Constants.REACTION_CHOSEN, self.get_khan_react_chosen())
                if self.get_khan_react_chosen() and not self.get_khan_react_chosen() == Constants.STATUS:
                    await chn.send(Constants.MSG_KHAN_OPEN_UPDATE.format(message.author) if self.bot.get_khan_active() else Constants.MSG_KHAN_CLOSE_UPDATE.format(message.author))
                else:
                    await chn.send(Constants.MSG_KHAN_STATUS.format(Constants.ACTIVE if self.bot.get_khan_active() else Constants.INACTIVE))
            except asyncio.TimeoutError:
                logger.info(Constants.REACT_TIMEOUT, Constants.KHAN)
                await msg.delete()
        else:
            await chn.send(Constants.MSG_COMD_DENIED)

    @commands.command(name=Constants.WAR_L)
    async def toggle_war(self, message):
        chn = message.channel

        if is_creme_brulee(message.author.roles):
            msg = await chn.send(Constants.MSG_WAR_ENQUIRY)
            await add_msg_reactions(msg, Constants.UPDATE)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == Constants.EMOJI_STATUS:
                        logger.info(Constants.WAR_TRIGGER, Constants.STATUS, user.display_name)
                        self.set_war_react_chosen(Constants.STATUS)
                    if reaction.emoji == Constants.EMOJI_OPEN:
                        logger.info(Constants.WAR_TRIGGER, Constants.OPEN, user.display_name)
                        self.set_war_react_chosen(Constants.OPEN)
                        self.bot.set_war_active(True)
                    if reaction.emoji == Constants.EMOJI_CLOSE:
                        logger.info(Constants.WAR_TRIGGER, Constants.CLOSE, user.display_name)
                        self.set_war_react_chosen(Constants.CLOSE)
                        self.bot.set_war_active(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for(Constants.REACTION_ADD, timeout=Constants.REACTION_TIMEOUT_SECONDS, check=check)
                await msg.delete()
                logger.info(Constants.REACTION_CHOSEN, self.get_war_react_chosen())
                if self.get_war_react_chosen() and not self.get_war_react_chosen() == Constants.STATUS:
                    await chn.send(Constants.MSG_WAR_OPEN_UPDATE.format(message.author) if self.bot.get_war_active() else Constants.MSG_WAR_CLOSE_UPDATE.format(message.author))
                else:
                    await chn.send(Constants.MSG_WAR_STATUS.format(Constants.ACTIVE if self.bot.get_war_active() else Constants.INACTIVE))
            except asyncio.TimeoutError:
                logger.info(Constants.REACT_TIMEOUT, Constants.NODE_WAR)
                await msg.delete()
        else:
            await chn.send(Constants.MSG_COMD_DENIED)

    @commands.command(name=Constants.SNIPE_L)
    async def receive_snipe_schedule(self, ctx):
        logger.info("Snipe schedule function invoked")
        if is_brioche_bun(ctx.message.author.roles):
            if ctx.message.attachments:
                logger.info("Snipe schedule attachment file received from %s", ctx.message.author.display_name)
                snipe_schedule  = ctx.message.attachments[0]
                await snipe_schedule.save(Constants.SNIPE_SCHEDULE_FILE)
            else:
                logger.info("No attachments, sending planned snipe schedules")
                schedules = []
                with open (Constants.SNIPE_SCHEDULE_FILE, Constants.FILE_READ_MODE) as snipe_duty_file:
                    data = csv.reader(snipe_duty_file, delimiter=",")
                    for line in data:
                        item = "{0}, {1}: {2}".format(line[0], line[4], line[1])
                        schedules.append(item)
                logger.info(schedules)
                await ctx.send('```{}```'.format('\n'.join(schedules)))
        else:
            logger.info("Member %s tried to call officer only snipe function", ctx.message.author.display_name)
            await ctx.send(Constants.MSG_COMD_DENIED)

    @commands.command(name=Constants.INTRO_L)
    async def send_intro_qn(self, ctx, msg):
        if is_brioche_bun(ctx.message.author.roles):
            about_us = self.bot.get_channel(Constants.ID_CHN_ABOUT_US)
            try:
                member = await self.bot.fetch_user(msg[3:-1])
                logger.info("{0} invoked intro for {1}".format(ctx.message.author.display_name, member.display_name))
                await ctx.send(Constants.MSG_REC_OPEN_MSG.format(member.mention, about_us))
            except NotFound:
                logger.info("Unknown user fetched by {0}, setting member to empty string and sending generic welcome message instead".format(ctx.message.author.display_name))
                member = None
            finally:
                await ctx.message.delete()
                await ctx.send(file=discord.File(Constants.ASSET_POSTER))
                await ctx.send(Constants.MSG_REC_OPEN_MSG.format(member.mention, about_us)) \
                if member else await ctx.send(Constants.MSG_REC_OPEN_MSG.format('', about_us))

        else:
            logger.warn("Member %s tried to call intro", ctx.message.author.display_name)

    def set_recruit_react_chosen(self, react: str) -> None:
        self.__recruit_react_chosen = react

    def get_recruit_react_chosen(self) -> str:
        return self.__recruit_react_chosen
    
    def set_khan_react_chosen(self, react: str) -> None:
        self.__khan_react_chosen = react

    def get_khan_react_chosen(self) -> str:
        return self.__khan_react_chosen

    def set_war_react_chosen(self, react: str) -> None:
        self.__war_react_chosen_chosen = react

    def get_war_react_chosen(self) -> str:
        return self.__war_react_chosen_chosen

def setup(bot):
    bot.add_cog(Officer(bot))