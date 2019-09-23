from discord.ext import commands
import discord

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
        print("Logged in as")
        print(self.bot.user.name)
        print(self.bot.user.id)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ctx = member.guild.system_channel
        if ctx is not None:
            await ctx.send('Welcome {0.mention} to Pastries!\n\n'
                           'Head over to #rules and change your discord nickname to your family name.\n'
                           'Enjoy your stay!'.format(member))

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
                      "%bug <message>- reports a bug to Kagi\n\n```")
        await ctx.send(content)

    @commands.command(name='bug')
    async def bug(self, ctx):
        await ctx.send('<@!{}> A bug have been discovered!'.format(self.bot.get_owner_id()))

    @commands.command(name='hystria')
    async def send_hyst_map(self, ctx):
        await ctx.send(file=discord.File('hystria.png'))
        
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
                await channel.send(file=discord.File('nezuko.gif'))
            elif content.startswith('%') and ctx.valid is False:
                results = self.bot.scraper.print_ingredients(content)
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
