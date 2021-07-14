from discord.ext import commands
from discord.utils import get
import asyncio, pendulum, Constants
from Logger import logger
from discord import File, User

class Announcement(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.ANNOUNCEMENT)
        self.bot = bot
        self.bot.loop.create_task(self.khan_announcement())
        self.bot.loop.create_task(self.war_announcement())
        self.__khan_react = None
        self.__war_react = None

    @commands.command(name=Constants.KHAN_L)
    async def toggle_khan(self, message):
        author_roles = message.author.roles
        chn = message.channel

        if Constants.ID_ROLE_CREME in [role.id for role in author_roles]:
            status_emoji = Constants.EMOJI_STATUS
            open_emoji = Constants.EMOJI_OPEN
            close_emoji = Constants.EMOJI_CLOSE
            msg = await chn.send(Constants.MSG_KHAN_ENQUIRY)
            await msg.add_reaction(status_emoji)
            await msg.add_reaction(open_emoji)
            await msg.add_reaction(close_emoji)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == status_emoji:
                        logger.info(Constants.KHAN_TRIGGER, Constants.OPEN, user.display_name)
                        self.__khan_react = Constants.STATUS
                    if reaction.emoji == open_emoji:
                        logger.info(Constants.KHAN_TRIGGER, Constants.OPEN, user.display_name)
                        self.__khan_react = Constants.OPEN
                        self.bot.set_khan_active(True)
                    if reaction.emoji == close_emoji:
                        logger.info(Constants.KHAN_TRIGGER, Constants.OPEN, user.display_name)
                        self.__khan_react = Constants.CLOSE
                        self.bot.set_khan_active(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for(Constants.REACTION_ADD, timeout=Constants.REACTION_TIMEOUT_SECONDS, check=check)
                await msg.delete()
                logger.info(Constants.REACTION_CHOSEN, self.__khan_react)
                if self.__khan_react == Constants.OPEN or self.__khan_react == Constants.CLOSE:
                    if self.bot.get_khan_active():
                        await chn.send(Constants.MSG_KHAN_OPEN_UPDATE.format(message.author))
                    if not self.bot.get_khan_active():
                        await chn.send(Constants.MSG_KHAN_CLOSE_UPDATE.format(message.author))
                else:
                    await chn.send(Constants.MSG_KHAN_STATUS.format(Constants.ACTIVE if self.bot.get_khan_active() else Constants.INACTIVE))
            except asyncio.TimeoutError:
                logger.info(Constants.REACT_TIMEOUT, Constants.KHAN)
                await msg.delete()
        else:
            await chn.send(Constants.MSG_COMD_DENIED)

    @commands.command(name=Constants.WAR_L)
    async def toggle_war(self, message):
        author_roles = message.author.roles
        chn = message.channel

        if Constants.ID_ROLE_CREME in [role.id for role in author_roles]:
            status_emoji = Constants.EMOJI_STATUS
            open_emoji = Constants.EMOJI_OPEN
            close_emoji = Constants.EMOJI_CLOSE
            msg = await chn.send(Constants.MSG_WAR_ENQUIRY)
            await msg.add_reaction(status_emoji)
            await msg.add_reaction(open_emoji)
            await msg.add_reaction(close_emoji)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == status_emoji:
                        logger.info(Constants.WAR_TRIGGER, Constants.STATUS, user.display_name)
                        self.__war_react = Constants.STATUS
                    if reaction.emoji == open_emoji:
                        logger.info(Constants.WAR_TRIGGER, Constants.OPEN, user.display_name)
                        self.__war_react = Constants.OPEN
                        self.bot.set_war_active(True)
                    if reaction.emoji == close_emoji:
                        logger.info(Constants.WAR_TRIGGER, Constants.CLOSE, user.display_name)
                        self.__war_react = Constants.CLOSE
                        self.bot.set_war_active(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for(Constants.REACTION_ADD, timeout=Constants.REACTION_TIMEOUT_SECONDS, check=check)
                await msg.delete()
                logger.info(Constants.REACTION_CHOSEN, self.__war_react)
                if self.__war_react == Constants.OPEN or self.__war_react == Constants.CLOSE:
                    if self.bot.get_war_active():
                        await chn.send(Constants.MSG_WAR_OPEN_UPDATE.format(message.author))
                    if not self.bot.get_war_active():
                        await chn.send(Constants.MSG_WAR_CLOSE_UPDATE.format(message.author))
                else:
                    await chn.send(Constants.MSG_WAR_STATUS.format(Constants.ACTIVE if self.bot.get_khan_active() else Constants.INACTIVE))
            except asyncio.TimeoutError:
                logger.info(Constants.REACT_TIMEOUT, Constants.NODE_WAR)
                await msg.delete()
        else:
            await chn.send(Constants.MSG_COMD_DENIED)


    @commands.Cog.listener()
    async def khan_announcement(self):
        logger.info(Constants.SCHEDULER_STARTUP, Constants.KHAN_ANNC)
        next_khan_annc = pendulum.today().next(pendulum.FRIDAY).add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
        self.bot.set_next_khan_annc(next_khan_annc)
        logger.info(Constants.NEXT_ANNC, Constants.KHAN, self.bot.get_next_khan_annc().strftime(Constants.DT_FORMAT_ANNC))

        await self.bot.wait_until_ready()
        chn = self.bot.get_channel(Constants.ID_CHN_MENU_BOARD)

        while not self.bot.is_closed():
            if pendulum.now().set(microsecond=Constants.ZERO) == self.bot.get_next_khan_annc():
                if self.bot.get_khan_active():
                    logger.info(Constants.SENT_ANNC, Constants.KHAN, pendulum.now().strftime(Constants.DT_FORMAT_ANNC))

                    el = await self.bot.fetch_user(Constants.ID_USER_EL)
                    await chn.send(file=File(Constants.ASSET_KHAN_ANNC))
                    msg = await chn.send(Constants.MSG_KHAN_INVITE.format(self.get_next_khan_dt().format(Constants.DT_FORMAT_INVITE), el))
                    await msg.add_reaction(Constants.EMOJI_Y)
                    await msg.add_reaction(Constants.EMOJI_N)

                    logger.info(Constants.UPCOMING_ANNC, Constants.KHAN, self.get_next_khan_dt().strftime(Constants.DT_FORMAT_ANNC))

                    next_khan_annc = pendulum.today().next(pendulum.FRIDAY).add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
                    self.bot.set_next_khan_annc(next_khan_annc)
                    logger.info(Constants.NEXT_ANNC, Constants.KHAN, self.bot.get_next_khan_annc().strftime(Constants.DT_FORMAT_ANNC))
                else:
                    logger.info(Constants.INACTIVE_ANNOUNCER, Constants.KHAN)
            await asyncio.sleep(1)

    @commands.Cog.listener()
    async def war_announcement(self):
        logger.info(Constants.SCHEDULER_STARTUP, Constants.NODE_WAR)
        next_war_annc = pendulum.today().next(pendulum.WEDNESDAY).add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
        self.bot.set_next_war_annc(next_war_annc)
        logger.info(Constants.NEXT_ANNC, Constants.NODE_WAR, self.bot.get_next_war_annc().strftime(Constants.DT_FORMAT_ANNC))

        await self.bot.wait_until_ready()
        chn = self.bot.get_channel(Constants.ID_CHN_MENU_BOARD)

        while not self.bot.is_closed():
            # logger.info("Comparing now: " + pendulum.now().strftime('%H:%M:%S') + " to next time: " + self.bot.get_next_war_annc().strftime('%H:%M:%S'))
            if pendulum.now().set(microsecond=Constants.ZERO) == self.bot.get_next_war_annc():
                if self.bot.get_war_active():
                    discussion_chn = self.bot.get_channel(Constants.ID_CHN_ACTIV_DISCUSS)
                    logger.info(Constants.SENT_ANNC, Constants.NODE_WAR, pendulum.now().strftime(Constants.DT_FORMAT_ANNC))
                    await chn.send(file=File(Constants.ASSET_NW_ANNC))
                    msg = await chn.send(Constants.MSG_WAR_INVITE.format(self.get_next_war_dt().format(Constants.DT_FORMAT_INVITE), discussion_chn))
                    await msg.add_reaction(Constants.EMOJI_Y)
                    await msg.add_reaction(Constants.EMOJI_N)

                    logger.info(Constants.UPCOMING_ANNC, Constants.NODE_WAR, self.get_next_war_dt().strftime(Constants.DT_FORMAT_ANNC))

                    next_war_annc = pendulum.today().next(pendulum.WEDNESDAY).add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
                    self.bot.set_next_war_annc(next_war_annc)
                    logger.info(Constants.NEXT_ANNC, Constants.NODE_WAR, self.bot.get_next_war_annc().strftime(Constants.DT_FORMAT_ANNC))
                else:
                    logger.info(Constants.INACTIVE_ANNOUNCER, Constants.NODE_WAR)
            await asyncio.sleep(1)

    def get_next_khan_dt(self):
        return self.bot.get_next_khan_annc().next(pendulum.SATURDAY).add(hours=Constants.TWENTY_ONE)

    def get_next_war_dt(self):
        return self.bot.get_next_war_annc().next(pendulum.SUNDAY).add(hours=Constants.TWENTY_ONE)

def setup(bot):
    bot.add_cog(Announcement(bot))
