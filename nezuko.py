import discord
from Scraper import Scraper
from data import FAILSTACK, getday

scraper = Scraper()
nezuko = discord.Client()
TOKEN = ''

@nezuko.event
async def on_message(message):
    msg = message.content.lower()
    chnl = message.channel
    reply=''

    if message.author == nezuko.user:
        return
    if 'nezuko' in msg:
        await chnl.send(file=discord.File('nezuko.gif'))
    if 'hello' in msg:
        await chnl.send("Hello {0.author.mention}!".format(message))
    if msg.startswith('%'):
        if msg == '%help':
            reply = "List of commands\n" \
                    "----------------\n" \
                    "%help - shows this message\n" \
                    "%foodname - retrieves ingredients i.e. %5 beer\n" \
                    "%wb - shows world boss info\n" \
                    "%fs - shows the failstack chart\n" \
                    "%bug <message>- reports a bug to Kagi\n"

        elif '%bug' in msg:
            await chnl.send('<@!382152478810046464>')
        elif msg == '%fs':
            reply = FAILSTACK
        elif msg == '%wb':
            reply = "Work in progress"
        else:
            results = scraper.print_ingredients(msg)
            if not results:
                reply = "Item not found! This bot is still a work in progress so some stuff might not work :(\nPerhaps you wanna use '%help'?"
            else:
                reply = '\n'.join(results)
        await chnl.send('```' + reply + '```')


@nezuko.event
async def on_ready():
    print("Logged in as")
    print(nezuko.user.name)
    print(nezuko.user.id)


nezuko.run(TOKEN)
