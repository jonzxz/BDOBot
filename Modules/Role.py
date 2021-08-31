class Role(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.ROLE)
        self.bot = bot

    @commands.command(name=Constants.BOSSHUNTER_L)
    async def set_bh_role(self, message):
        role = get(message.guild.roles, id=Constants.ID_ROLE_BOSSHUNTER)
        member = message.author
        chn = message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send(Constants.MSG_ROLE_REGISTER.format(message, Constants.BOSS_HUNTER))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send(Constants.MSG_ROLE_RESIGN.format(message, Constants.BOSS_HUNTER))

    @commands.command(name=Constants.POPCORN_L)
    async def set_popcorn_role(self, message):
        role = get(message.guild.roles, id = Constants.ID_ROLE_POPCORN)
        member = message.author
        chn = message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send(Constants.MSG_ROLE_REGISTER.format(message, Constants.CARAMEL_POPCORN))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send(Constants.MSG_ROLE_RESIGN.format(message, Constants.CARAMEL_POPCORN))

    @commands.command(name=Constants.DOUGHTART_L)
    async def set_dota_role(self, message):
        role = get(message.guild.roles, id = Constants.ID_ROLE_DOUGHTART)
        member = message.author
        chn = message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send(Constants.MSG_ROLE_REGISTER.format(message, Constants.DOUGHTART))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send(Constants.MSG_ROLE_RESIGN.format(message, Constants.DOUGHTART))

def setup(bot):
    bot.add_cog(Role(bot))