from utils import add_msg_reactions, is_creme_brulee
from discord.ext import commands
import discord, asyncio, re, emoji, Constants, pendulum
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
        self.bot.loop.create_task(self.update_roles())

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

        if is_creme_brulee(message.author.roles):
            msg = await chn.send(Constants.MSG_RECRUIT_ENQUIRY)
            await add_msg_reactions(msg, Constants.UPDATE)

            def check(reaction, user):
                if user == message.author:
                    if reaction.emoji == Constants.EMOJI_STATUS:
                        logger.info(Constants.RECRUIT_TRIGGER, Constants.STATUS, user.display_name)
                        self.react_chosen = Constants.STATUS
                    if reaction.emoji == Constants.EMOJI_OPEN:
                        logger.info(Constants.RECRUIT_TRIGGER, Constants.STATUS, user.display_name)
                        self.react_chosen = Constants.OPEN
                        self.bot.set_recruit_open(True)
                    if reaction.emoji == Constants.EMOJI_CLOSE:
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
                if self.react_chosen and not self.react_chosen == Constants.STATUS:
                    await chn.send(Constants.MSG_RECRUIT_OPEN_UPDATE.format(message.author) if self.bot.get_recruit_open() else Constants.MSG_RECRUIT_CLOSE_UPDATE.format(message.author))
                else:
                    await chn.send(Constants.MSG_RECRUIT_STATUS.format(Constants.OPEN if self.bot.get_recruit_open() else Constants.CLOSE))
            except asyncio.TimeoutError:
                logger.info(Constants.REACT_TIMEOUT, Constants.RECRUIT)
                await msg.delete()
        else:
            await chn.send(Constants.MSG_COMD_DENIED)

    @commands.Cog.listener()
    async def update_roles(self):
        logger.info(Constants.SCHEDULER_STARTUP, Constants.ROLE_UPDATE)
        if pendulum.now() >= pendulum.today().add(hours=Constants.EIGHTEEN):
            next_execution = pendulum.tomorrow().add(hours=18, minutes=0, seconds=0, microseconds=0)
        else:
            next_execution = pendulum.today().add(hours=18, minutes=0, seconds=0, microseconds=0)
        logger.info(Constants.NEXT_ROLE_UPDATE_TIME, next_execution.strftime(Constants.DT_FORMAT_ANNC))

        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            # logger.info("Comparing now: " + pendulum.now().strftime('%H:%M:%S') + " to next time: " + next_execution.strftime('%H:%M:%S'))

            if pendulum.now().set(microsecond=Constants.ZERO) == next_execution:
                guild = self.bot.get_guild(id=Constants.ID_SERVER_PASTRIES)
                croissant_role = get(guild.roles, id = Constants.ID_ROLE_CROISSANT)
                gmember_role = get(guild.roles, id = Constants.ID_ROLE_GMEMBER)
                macaron_role = get(guild.roles, id = Constants.ID_ROLE_MACARON)
                eggtart_role = get(guild.roles, id = Constants.ID_ROLE_EGGTART)
                # brioche_role = get(message.guild.roles, id = Constants.ID_ROLE_BRIOCHE)
                # creme_role = get(message.guild.roles, id = Constants.ID_ROLE_CREME)
                # officer_role = get(message.guild.roles, id = Constants.ID_ROLE_OFFICER)
                # gm_role = get(guild.roles, id = Constants.ID_ROLE_GM)
                member_role_add = []
                member_role_removed = []
                for member in guild.members:
                    # Feature to update creme brulee / brioche such that all croissants are removed
                    # if (creme_role in member.roles or brioche_role in member.roles) and not gm_role in member.roles:
                    #     if croissant_role in member.roles:
                    #         logger.info("officer %s has croissant role, removing", member.display_name)
                    #         # await member.remove_roles(croissant_role)
                    #     if not officer_role in member.roles:
                    #         logger.info("officer %s does not have officer role, adding", member.display_name)
                    #         # await member.add_roles(officer_role)
                    if croissant_role in member.roles and not gmember_role in member.roles:
                        member_role_add.append(member.display_name)
                        await member.add_roles(gmember_role)
                    if (macaron_role in member.roles or eggtart_role in member.roles) and gmember_role in member.roles:
                        await member.remove_roles(gmember_role)
                        member_role_removed.append(member.display_name)

                member_role_added_str = ', '.join(member for member in member_role_add)
                member_role_removed_str = ', '.join(member for member in member_role_removed)
                chn = self.bot.get_channel(Constants.ID_CHN_BOT_CHN)
                if member_role_add:
                    logger.info(Constants.ROLE_UPDATED, Constants.CROISSANT, Constants.GUILD_MEMBER, Constants.ADDED, member_role_added_str)
                    await chn.send(Constants.MSG_ROLE_UPDATE.format(Constants.CROISSANT, Constants.GUILD_MEMBER, Constants.ADDED, member_role_added_str))
                else:
                    logger.info(Constants.NO_ROLE_UPDATED, Constants.GUILD_MEMBER)
                if member_role_removed:
                    logger.info(Constants.ROLE_UPDATED, '/'.join([Constants.MACARON, Constants.EGGTART]), Constants.GUILD_MEMBER, Constants.REMOVED, member_role_removed_str)
                    await chn.send(Constants.MSG_ROLE_UPDATE.format('/'.join([Constants.MACARON, Constants.EGGTART]), Constants.GUILD_MEMBER, Constants.REMOVED, member_role_removed_str))
                else:
                    logger.info(Constants.NO_ROLE_UPDATED, Constants.GUILD_MEMBER)
                next_execution = pendulum.tomorrow().add(hours=Constants.EIGHTEEN)
                logger.info("setting next role update execution to %s", next_execution.strftime(Constants.DT_FORMAT_ANNC))
            await asyncio.sleep(1)

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
