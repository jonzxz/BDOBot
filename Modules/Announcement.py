from discord.ext import commands
from discord.utils import get
import asyncio, pendulum
from Logger import logger
from discord import File, User

class Announcement(commands.Cog):
    def __init__(self, bot):
        logger.info("starting up Announcement Cog")
        self.bot = bot
        self.bot.loop.create_task(self.khan_announcement())
        self.bot.loop.create_task(self.war_announcement())
        self.__khan_react = None
        self.__war_react = None

    @commands.command(name='khan')
    async def toggle_khan(self, message):
        author_roles = message.author.roles
        chn = message.channel

        if self.bot.get_officer_id() in [role.id for role in author_roles]:
            status_emoji = '\U0001f35e'
            open_emoji = '\U00002b55'
            close_emoji = '\U0000274c'
            msg = await chn.send('Please react to enquire or update Khan announcement status!\n\n' \
                            ':bread: - Khan Announcement Status\n\n:o: - Activate Khan Announcement \n\n:x: - Deactivate Khan Announcement')
            await msg.add_reaction(status_emoji)
            await msg.add_reaction(open_emoji)
            await msg.add_reaction(close_emoji)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == status_emoji:
                        logger.info("Khan: %s status triggered", user)
                        self.__khan_react = "STATUS"
                    if reaction.emoji == open_emoji:
                        logger.info("Khan: activate triggered")
                        self.__khan_react = "OPEN"
                        self.bot.set_khan_active(True)
                    if reaction.emoji == close_emoji:
                        logger.info("Khan: deactivate triggered")
                        self.__khan_react = "CLOSE"
                        self.bot.set_khan_active(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=7, check=check)
                await msg.delete()
                logger.info("Khan REACT_CHOSEN %s", self.__khan_react)
                if self.__khan_react == "OPEN" or self.__khan_react == "CLOSE":
                    if self.bot.get_khan_active():
                        await chn.send("{0.mention} ```Updated Khan Announcement status to active!```".format(message.author))
                    if not self.bot.get_khan_active():
                        await chn.send("{0.mention} ```Updated Khan Announcement status to inactive!```".format(message.author))
                else:
                    await chn.send("```Khan Announcement Status: {0}```".format("ACTIVE" if self.bot.get_khan_active() else "INACTIVE"))
            except asyncio.TimeoutError:
                logger.info("Khan: hit timeout, removing message")
                await msg.delete()
        else:
            await chn.send("```Only Crème brûlées are allowed to use this feature!```")

    @commands.command(name='war')
    async def toggle_war(self, message):
        author_roles = message.author.roles
        chn = message.channel

        if self.bot.get_officer_id() in [role.id for role in author_roles]:
            status_emoji = '\U0001f35e'
            open_emoji = '\U00002b55'
            close_emoji = '\U0000274c'
            msg = await chn.send('Please react to enquire or update NW announcement status!\n\n' \
                            ':bread: - NW Announcement Status\n\n:o: - Activate NW Announcement \n\n:x: - Deactivate NW Announcement')
            await msg.add_reaction(status_emoji)
            await msg.add_reaction(open_emoji)
            await msg.add_reaction(close_emoji)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == status_emoji:
                        logger.info("NW: %s status triggered", user)
                        self.__war_react = "STATUS"
                    if reaction.emoji == open_emoji:
                        logger.info("NW: activate triggered")
                        self.__war_react = "OPEN"
                        self.bot.set_war_active(True)
                    if reaction.emoji == close_emoji:
                        logger.info("NW: deactivate triggered")
                        self.__war_react = "CLOSE"
                        self.bot.set_war_active(False)
                    return True
                return False

            await asyncio.sleep(1)

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=7, check=check)
                await msg.delete()
                logger.info("War REACT_CHOSEN %s", self.__war_react)
                if self.__war_react == "OPEN" or self.__war_react == "CLOSE":
                    if self.bot.get_war_active():
                        await chn.send("{0.mention} ```Updated War Announcement status to active!```".format(message.author))
                    if not self.bot.get_war_active():
                        await chn.send("{0.mention} ```Updated War Announcement status to inactive!```".format(message.author))
                else:
                    await chn.send("```War Announcement Status: {0}```".format("ACTIVE" if self.bot.get_khan_active() else "INACTIVE"))
            except asyncio.TimeoutError:
                logger.info("NW: hit timeout, removing message")
                await msg.delete()
        else:
            await chn.send("```Only Crème brûlées are allowed to use this feature!```")


    @commands.Cog.listener()
    async def khan_announcement(self):
        logger.info("starting up Khan announcement scheduler")
        next_khan_annc = pendulum.today().next(pendulum.FRIDAY).add(hours=18, minutes=0, seconds=0)
        self.bot.set_next_khan_annc(next_khan_annc)
        logger.info("next Khan announcement set at: " + self.bot.get_next_khan_annc().strftime('%d/%m/%Y, %H:%M:%S'))

        await self.bot.wait_until_ready()
        chn = self.bot.get_channel(self.bot.get_menu_channelid())

        while not self.bot.is_closed():
            # logger.info("Comparing now: " + pendulum.now().strftime('%H:%M:%S') + " to next time: " + self.bot.get_next_khan_annc().strftime('%H:%M:%S'))
            if pendulum.now().set(microsecond=0) == self.bot.get_next_khan_annc():
                if self.bot.get_khan_active():
                    logger.info("sent Khan announcement at " + pendulum.now().strftime('%d/%m/%y %H:%M:%S'))

                    el = await self.bot.fetch_user(193314826779361281)
                    await chn.send(file=File('assets/KHAN_ANN.png'))
                    msg = await chn.send(':whale:**HI BREADS! LET\'S DO KHAN RAID TOMOROWWW!!:whale:\n\n'
                    ':calendar_spiral:Mark your calendar!**\n'
                    '`{0} GMT+8`\n\n'
                    ':pretzel:Server will be announced later!\n'
                    ':pretzel:CTG to OE, and taxi back to mainland will be provided\n'
                    ':pretzel:We will be doing XL (Tier 3)!\n'
                    ':pretzel:Let us know if you have friends interested to come to WH!\n\n'
                    '*New to Khan? Just come and join uss! No gear req needed as you\'ll shoot em fish with cannon! >:D*\n'
                    'Check this Video Guide to learn about Cannon Rotation so you can deal damage to the big fish more efficiently!\n'
                    '> https://www.youtube.com/watch?v=h1jY7r6bGQk\n'
                    'Or kindly poke {1.mention} for your Khan related questions!\n\n'
                    '**Confirm your attendance**\n'
                    '> by reacting :regional_indicator_y: if you\'re going to attend, or :regional_indicator_n: if you\'re not!\n'
                    '*Don\'t miss out seeing El getting Khan\'s Heart! See you this Saturday, breados!*<:yay:707879651804053565>'
                    '<@&574641817505497106> <@&635776028048097290> <@&574641855229067264>'
                    .format(self.get_next_khan_dt().format('dddd DD MMM YYYY hh:mm A'), el)
                    )
                    await msg.add_reaction('\U0001F1FE')
                    await msg.add_reaction('\U0001F1F3')

                    logger.info("upcoming Khan raid announced for: " + self.get_next_khan_dt().strftime('%d/%m/%y %H:%M:%S'))

                    next_khan_annc = pendulum.today().next(pendulum.FRIDAY).add(hours=18, minutes=0, seconds=0)
                    self.bot.set_next_khan_annc(next_khan_annc)
                    logger.info("updated next Khan announcement to " + self.bot.get_next_khan_annc().strftime('%d/%m/%y %H:%M:%S'))
                else:
                    logger.info("Khan announcement timer hit: INACTIVE, no message sent")
            await asyncio.sleep(1)

    @commands.Cog.listener()
    async def war_announcement(self):
        logger.info("starting up War announcement scheduler")
        next_war_annc = pendulum.today().next(pendulum.WEDNESDAY).add(hours=18, minutes=0, seconds=0)
        self.bot.set_next_war_annc(next_war_annc)
        logger.info("next War announcement set at: " + self.bot.get_next_war_annc().strftime('%d/%m/%Y, %H:%M:%S'))

        await self.bot.wait_until_ready()
        chn = self.bot.get_channel(self.bot.get_menu_channelid())

        while not self.bot.is_closed():
            # logger.info("Comparing now: " + pendulum.now().strftime('%H:%M:%S') + " to next time: " + self.bot.get_next_war_annc().strftime('%H:%M:%S'))
            if pendulum.now().set(microsecond=0) == self.bot.get_next_war_annc():
                if self.bot.get_war_active():
                    discussion_chn = self.bot.get_channel(645931876107943967)
                    logger.info("sent War announcement at " + pendulum.now().strftime('%d/%m/%y %H:%M:%S'))

                    await chn.send(file=File('assets/NW_ANN.png'))
                    msg = await chn.send(':crossed_swords:**HI BREADS! IT\'S WAR TIME!!:crossed_swords:\n\n'
                    ':calendar_spiral:Mark your calendar!**\n'
                    '`{0} GMT+8`\n\n'
                    ':pretzel:Server will be announced later!\n'
                    ':pretzel:**No minimum gearscore required**, shotcalls will be on Discord so joining in voice chat is mandatory!<:kagi_proudmum:830388637073145907>\n'
                    ':pretzel:We will be participating in Tier 1 node war!\n\n'
                    '*New to Node War? Just come and join uss! Alternatively, Node War guides and discussions are on {1.mention}*\n\n'
                    'More details about the node and platoon composition will be posted here on war day!\n\n'
                    '**Confirm your attendance**\n'
                    '> by reacting :regional_indicator_y: if you\'re going to attend, or :regional_indicator_n: if you\'re not!\n'
                    '*With consideration of participant caps, members with :regional_indicator_y: reacted in this post will be guaranteed a slot*'
                    '<@&574641817505497106> <@&635776028048097290> <@&574641855229067264>'
                    .format(self.get_next_war_dt().format('dddd DD MMM YYYY hh:mm A'), discussion_chn)
                    )
                    await msg.add_reaction('\U0001F1FE')
                    await msg.add_reaction('\U0001F1F3')

                    logger.info("upcoming War raid announced for: " + self.get_next_war_dt().strftime('%d/%m/%y %H:%M:%S'))

                    next_war_annc = pendulum.today().next(pendulum.WEDNESDAY).add(hours=18, minutes=0, seconds=0)
                    self.bot.set_next_war_annc(next_war_annc)
                    logger.info("updated next War announcement to " + self.bot.get_next_war_annc().strftime('%d/%m/%y %H:%M:%S'))
                else:
                    logger.info("War announcement timer hit: INACTIVE, no message sent")
            await asyncio.sleep(1)

    def get_next_khan_dt(self):
        return self.bot.get_next_khan_annc().next(pendulum.SATURDAY).add(hours=21)

    def get_next_war_dt(self):
        return self.bot.get_next_war_annc().next(pendulum.SUNDAY).add(hours=21)

def setup(bot):
    bot.add_cog(Announcement(bot))
