from discord.ext import commands
import discord, asyncio, Constants
from Logger import logger
from discord.utils import get
from utils import add_msg_reactions, equals

class Role(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.ROLE)
        self.bot = bot

    @commands.command(name=Constants.ROLE_L)
    async def update_role(self, ctx):
        msg = await ctx.send(Constants.MSG_ROLE_MENU.format(ctx.message.author, Constants.EMOJI_EL_SIP_C, Constants.EMOJI_BAM_MAD_C, Constants.EMOJI_EL_YAY_C, Constants.EMOJI_MIIA_GASP_C))
        await add_msg_reactions(msg, Constants.ROLES_UPDATE_COMD)

        def check(reaction, user):
            return equals(user, ctx.message.author)
        
        await asyncio.sleep(1)

        try:
            reaction, user = await self.bot.wait_for(Constants.REACTION_ADD, timeout=Constants.THIRTY, check=check)
            if equals(user, ctx.message.author):
                el_sip_emoji = self.bot.get_emoji(Constants.EMOJI_EL_SIP_C_ID)
                bam_mad_emoji = self.bot.get_emoji(Constants.EMOJI_BAM_MAD_C_ID)
                el_yay_emoji = self.bot.get_emoji(Constants.EMOJI_EL_YAY_C_ID)
                miia_gasp_emoji = self.bot.get_emoji(Constants.EMOJI_MIIA_GASP_C_ID)

                if equals(reaction.emoji, el_sip_emoji):
                    logger.info("%s (un)registered as a %s", ctx.message.author.display_name, Constants.CARAMEL_POPCORN)
                    await self.set_popcorn_role(ctx)
                if equals(reaction.emoji, bam_mad_emoji):
                    logger.info("%s (un)registered as a %s", ctx.message.author.display_name, Constants.DOUGHTART)
                    await self.set_dota_role(ctx)
                if equals(reaction.emoji, el_yay_emoji):
                    logger.info("%s (un)registered as a %s", ctx.message.author.display_name, Constants.DND_CRUMBS)
                    await self.set_dnd_role(ctx)
                if equals(reaction.emoji, miia_gasp_emoji):
                    logger.info("%s (un)registered as a %s", ctx.message.author.display_name, Constants.BOSS_HUNTER)
                    await self.set_bh_role(ctx)
            await msg.delete() 
        except asyncio.TimeoutError:
            await msg.delete()

    async def set_popcorn_role(self, ctx):
        role = get(ctx.message.guild.roles, id = Constants.ID_ROLE_POPCORN)
        member = ctx.message.author
        chn = ctx.message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send(Constants.MSG_ROLE_REGISTER.format(member, Constants.CARAMEL_POPCORN))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send(Constants.MSG_ROLE_RESIGN.format(member, Constants.CARAMEL_POPCORN))

    async def set_dota_role(self, ctx):
        role = get(ctx.message.guild.roles, id = Constants.ID_ROLE_DOUGHTART)
        member = ctx.message.author
        chn = ctx.message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send(Constants.MSG_ROLE_REGISTER.format(member, Constants.DOUGHTART))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send(Constants.MSG_ROLE_RESIGN.format(member, Constants.DOUGHTART))

    async def set_dnd_role(self, ctx):
        role = get(ctx.message.guild.roles, id=Constants.ID_ROLE_DND_CRUMBS)
        member = ctx.message.author
        chn = ctx.message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send(Constants.MSG_ROLE_REGISTER.format(member, Constants.DND_CRUMBS))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send(Constants.MSG_ROLE_RESIGN.format(member, Constants.DND_CRUMBS))

    async def set_bh_role(self, ctx):
        role = get(ctx.message.guild.roles, id=Constants.ID_ROLE_BOSSHUNTER)
        member = ctx.message.author
        chn = ctx.message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send(Constants.MSG_ROLE_REGISTER.format(member, Constants.BOSS_HUNTER))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send(Constants.MSG_ROLE_RESIGN.format(member, Constants.BOSS_HUNTER))

def setup(bot):
    bot.add_cog(Role(bot))