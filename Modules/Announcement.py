from discord.ext import commands
from discord.utils import get
import asyncio, pendulum, csv, Constants
from Logger import logger
from discord import File, User
from datetime import datetime
from utils import add_msg_reactions, is_creme_brulee

class Announcement(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.ANNOUNCEMENT)
        self.bot = bot
        self.bot.loop.create_task(self.khan_announcement())
        self.bot.loop.create_task(self.war_announcement())
        self.bot.loop.create_task(self.snipe_reminder())

    @commands.Cog.listener()
    async def khan_announcement(self):
        logger.info(Constants.SCHEDULER_STARTUP, Constants.KHAN_ANNC)
        next_khan_annc = self.calc_next_annc_dt(Constants.KHAN_CAPS)
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
                    await add_msg_reactions(msg, Constants.YES_NO)

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
        next_war_annc = self.calc_next_annc_dt(Constants.WAR_CAPS)
        self.bot.set_next_war_annc(next_war_annc)
        logger.info(Constants.NEXT_ANNC, Constants.NODE_WAR, self.bot.get_next_war_annc().strftime(Constants.DT_FORMAT_ANNC))

        await self.bot.wait_until_ready()
        chn = self.bot.get_channel(Constants.ID_CHN_MENU_BOARD)
        while not self.bot.is_closed():
            # logger.info("Comparing now: " + pendulum.now().strftime('%H:%M:%S') + " to next time: " + self.bot.get_next_war_annc().strftime('%H:%M:%S'))
            if pendulum.now().set(microsecond=Constants.ZERO) == self.bot.get_next_war_annc():
                if self.bot.get_war_active():
                    gear_class_chn = self.bot.get_channel(Constants.ID_CHN_GEAR_CLASS)
                    discussion_chn = self.bot.get_channel(Constants.ID_CHN_ACTIV_DISCUSS)
                    logger.info(Constants.SENT_ANNC, Constants.NODE_WAR, pendulum.now().strftime(Constants.DT_FORMAT_ANNC))
                    await chn.send(file=File(Constants.ASSET_NW_ANNC))
                    msg = await chn.send(Constants.MSG_WAR_INVITE.format(self.get_next_war_dt().format(Constants.DT_FORMAT_INVITE), discussion_chn, gear_class_chn))
                    await add_msg_reactions(msg, Constants.YES_NO)

                    logger.info(Constants.UPCOMING_ANNC, Constants.NODE_WAR, self.get_next_war_dt().strftime(Constants.DT_FORMAT_ANNC))

                    next_war_annc = pendulum.today().next(pendulum.WEDNESDAY).add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
                    self.bot.set_next_war_annc(next_war_annc)
                    logger.info(Constants.NEXT_ANNC, Constants.NODE_WAR, self.bot.get_next_war_annc().strftime(Constants.DT_FORMAT_ANNC))
                else:
                    logger.info(Constants.INACTIVE_ANNOUNCER, Constants.NODE_WAR)
            await asyncio.sleep(1)

    def retrieve_snipe_duty_today(self):
        today_str = pendulum.today().format(Constants.DT_FORMAT_SNIPE)

        with open(Constants.SNIPE_SCHEDULE_FILE, 'r') as snipe_duty_file:
            data = csv.reader(snipe_duty_file, delimiter=',')
            for line in data:
                if line[0] == today_str:
                    logger.info("Snipe duty today: %s, notification preference: %s", line[1], line[3])
                    self.bot.set_snipe_duty_officer_today(line[1], line[2], line[3])
                    return
            logger.error("No data for today %s, defaulting to None", pendulum.today().format(Constants.DT_FORMAT_SNIPE))
            self.bot.set_snipe_duty_officer_today(None)

    @commands.Cog.listener()
    async def snipe_reminder(self):
        logger.info(Constants.SCHEDULER_STARTUP, Constants.SNIPE_REMINDER)
        self.retrieve_snipe_duty_today()

        await self.bot.wait_until_ready()
        chn = self.bot.get_channel(Constants.ID_CHN_BOT_CHN)

        while not self.bot.is_closed():
            #logger.info("Comparing now: " + pendulum.now().strftime('%H:%M:%S'))
            # Updates at 12am
            if pendulum.now().set(microsecond=Constants.ZERO) == pendulum.today().add(hours=0, minutes=0, seconds=1):
                self.retrieve_snipe_duty_today()
                logger.info("Updating snipe duty, today's duty: %s", self.get_snipe_duty_person()[0])

            # Sends reminder
            if pendulum.now().set(microsecond=Constants.ZERO) == pendulum.today().add(hours=17, minutes=30, seconds=0):
                snipe_officer_details = self.bot.get_snipe_duty_officer_today()
                if snipe_officer_details:
                    if snipe_officer_details[2] == 'Y':
                        duty_officer = await self.bot.fetch_user(snipe_officer_details[1])
                        logger.info(Constants.SENT_ANNC, Constants.SNIPE_REMINDER, pendulum.now().strftime(Constants.DT_FORMAT_ANNC))
                        msg = await chn.send("{0.mention}\n```You are on snipe duty today, if you are unavailable, please ask other officers to take over!```".format(duty_officer))
                        #await add_msg_reactions(msg, Constants.YES_NO)
                else:
                    logger.error("No snipe duty determined for today.")
            await asyncio.sleep(1)


    def get_next_khan_dt(self):
        return self.bot.get_next_khan_annc().next(pendulum.SATURDAY).add(hours=Constants.SIXTEEN)

    def get_next_war_dt(self):
        return self.bot.get_next_war_annc().next(pendulum.SUNDAY).add(hours=Constants.TWENTY_ONE)

    def calc_next_annc_dt(self, annc_type: str) -> datetime:
        if (annc_type == Constants.WAR_CAPS):
            if pendulum.today().day_of_week == pendulum.WEDNESDAY and pendulum.now() <= pendulum.today().add(hours=Constants.EIGHTEEN):
                return pendulum.today().add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
            else:
                return pendulum.today().next(pendulum.WEDNESDAY).add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
        if (annc_type == Constants.KHAN_CAPS):
            if pendulum.today().day_of_week == pendulum.FRIDAY and pendulum.now() <= pendulum.today().add(hours=Constants.EIGHTEEN):
                return pendulum.today().add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
            else:
                return pendulum.today().next(pendulum.FRIDAY).add(hours=Constants.EIGHTEEN, minutes=Constants.ZERO, seconds=Constants.ZERO)
        return None

def setup(bot):
    bot.add_cog(Announcement(bot))
