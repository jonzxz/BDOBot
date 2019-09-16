from Scraper import Scraper
import discord
from discord.ext import commands
from utils import nextboss, mpcheck, get_token, timediff
from discord.utils import get, find
import asyncio




def start():
    nezuko = commands.Bot(command_prefix='%')
    scraper = Scraper()
    nezuko.remove_command('help')

    @nezuko.event
    async def on_ready():
        print("Logged in as")
        print(nezuko.user.name)
        print(nezuko.user.id)

    @nezuko.event
    async def on_member_join(member):
        chn = nezuko.get_channel(574641679575941137)
        await chn.send('Welcome ' + member.mention + ' to Pastries!\n\n Head over to #rules and change your discord nickname to your family name.\nEnjoy your stay!')

    @nezuko.command()
    async def bosshunter(message):
        role = get(message.guild.roles, name='Boss Hunter')
        member = message.author
        chn = message.channel
        bh = find(lambda r: r.name == 'Boss Hunter', member.roles)
        if bh is None:
            await member.add_roles(role)
            await chn.send("{0.author.mention} is now registered as a boss hunter!".format(message))
        else:
            await member.remove_roles(role)
            await chn.send("{0.author.mention} have resigned as a boss hunter!".format(message))


    @nezuko.event
    async def change_presence():
        await nezuko.wait_until_ready()
        while True:
            await nezuko.change_presence(activity=discord.Activity(name='Pastries', type=3))
            await asyncio.sleep(10)
            await nezuko.change_presence(activity=discord.Activity(name='use %help', type=1))
            await asyncio.sleep(10)


    @nezuko.event
    async def boss_reminder():
        await nezuko.wait_until_ready()
        # pastries boss hunter
        chn = nezuko.get_channel(574646616489721887)
        for role in nezuko.get_guild(574641536214630401).roles:
            if role.name == 'Boss Hunter':
                bh = role
        while not nezuko.is_closed():
            if timediff(nextboss().get_time()) == 1800:
                await chn.send(bh.mention + ', ' + nextboss().get_name() + ' will spawn in 30 minutes time!')
            await asyncio.sleep(1)

    @nezuko.command()
    async def help(chn):
        helpmsg = "```\n" \
                  "List of commands\n" \
                "----------------\n" \
                "%help - shows this message\n" \
                "%foodname - retrieves ingredients i.e. %5 beer\n" \
                "%wb - shows the upcoming world boss\n" \
                "%bosshunter - (un)register the Boss Hunter role. Receive notifications 30 minutes before world boss!\n" \
                "%mp - shows profit with(out) VP from selling in MP i.e. %mp 43500000\n" \
                "%bug <message>- reports a bug to Kagi\n" \
                "```"
        await chn.send(helpmsg)

    @nezuko.command()
    async def wb(chn):
        msg = ('The next boss is ' + nextboss().get_name() + ' at ' + nextboss().get_time().strftime('%H:%M') + 'hrs, GMT+8')
        await chn.send('```' + msg + '```')


    @nezuko.command()
    async def mp(chn, silver):
        await chn.send('```' + (mpcheck(silver) + '```'))

    @nezuko.command()
    async def bug(chn):
        await chn.send('<@!382152478810046464>' + ' A bug have been discovered!')

    @nezuko.event
    async def on_message(message):
        msg = message.content.lower()
        chnl = message.channel
        ctx = await nezuko.get_context(message)
        if message.author != nezuko.user:
            if 'hello' in msg:
                await chnl.send("Hello {0.author.mention}!".format(message))
            if 'nezuko' in msg:
                await chnl.send(file=discord.File('nezuko.gif'))
            elif msg.startswith('%') and ctx.valid == False:
                results = scraper.print_ingredients(msg)
                if not results:
                    reply = "I was not able to retrieve the results, make sure spelling is correct!\nPerhaps you wanna use '%help'?"
                else:
                    reply = '\n'.join(results)
                await chnl.send('```' + reply + '```')
            await nezuko.process_commands(message)
        else:
            return

    @nezuko.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error

    nezuko.loop.create_task(boss_reminder())
    nezuko.loop.create_task(change_presence())
    nezuko.run(get_token())
