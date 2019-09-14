from Scraper import Scraper
import discord
from discord.ext import commands
from utils import nextboss, mpcheck, get_token

def start():
    nezuko = commands.Bot(command_prefix='%')
    scraper = Scraper()
    nezuko.remove_command('help')

    @nezuko.event
    async def on_ready():
        print("Logged in as")
        print(nezuko.user.name)
        print(nezuko.user.id)

    @nezuko.command()
    async def on_member_join(chn, member):
        print("eee")
        await chn.send('Welcome ' + member + ' to Pastries!')

    @nezuko.command()
    async def help(chn):
        helpmsg = "```\n" \
                  "List of commands\n" \
                "----------------\n" \
                "%help - shows this message\n" \
                "%foodname - retrieves ingredients i.e. %5 beer\n" \
                "%wb - shows the upcoming world boss\n" \
                "%mp - shows profit with(out) VP from selling in MP i.e. %mp 43500000\n" \
                "%bug <message>- reports a bug to Kagi\n" \
                "```"
        await chn.send(helpmsg)

    @nezuko.command()
    async def wb(chn):
         await chn.send('```' + nextboss() + '```')

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

    nezuko.run(get_token())
