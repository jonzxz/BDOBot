from bs4 import BeautifulSoup
import requests, discord

headers = requests.utils.default_headers()

TOKEN = 'NjIwOTgwNzY1NjU1Njk1Mzcx.XXeupw.fczb3pTfNNfqVEgKvIzgX6d1-5g'

nezuko = discord.Client()

def initialization():
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

def create_data(name):
    url = "https://www.bdodae.com/items/index.php?item=" + name
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    raw_ingredients = []
    first = soup.find_all("div", {"class": "ing1_box"})
    for x in first:
        second = x.find_all("div", {"class": "ing1_item"})
        for y in second:
            raw_data = y.find_all("a", {"class": "item_popup"})
            for item in raw_data:
                if "(" and ")" in item.contents[0]:
                    raw_ingredients.append(item.contents[0])
    return raw_ingredients


def generate_results(name, multiples):
    name = clean_word(name)
    list = create_data(name)
    final = []
    for ingredient in list:
        count = clean_number(ingredient.split()[-1])
        name = remove_number(ingredient)
        count = int(count) * int(multiples)
        formatted = str(count) + " " + name
        final.append(formatted)
    return final

def clean_number(number):
    return number.replace("(", "").replace(")", "")

def clean_word(word):
    return word.strip().replace(" ", "_").replace(": ", "-")

def isdigit(word):
    return word.isdigit()

def remove_number(word):
    return ' '.join(word.split(' ')[:-1])

def print_ingredients(item):
    input = item
    if isdigit(input.split()[0]):
        space = ' '
        result = generate_results(space.join(input.split()[1:]), input.split()[0])
    else:
        input = clean_word(input)
        result = generate_results(input, 1)

    return result

#initialization()
#print(print_ingredients("beer"))

@nezuko.event
async def on_message(message):
    if message.author == nezuko.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hello {0.author.mention}".format(message))
    if message.content.startswith('%'):
        if message.content.startswith('%help'):
            nezukosays = "Type item name like '%beer' to search. All ingredients are for 1 unless you specify like '%500 beer'. Please report bugs to Kagi!"
        else:
            item = message.content.replace("%", "")
            #msg = 'Hello {0.author.mention}'.format(message)

            results = print_ingredients(item)
            if not results:
                results = "Item not found! This bot is still a work in progress so some stuff might not work :(, perhaps you wanna use '%help'?"
            else:
                results = '\n'.join(results)
            nezukosays = results
        await message.channel.send("```" + nezukosays + "```")


@nezuko.event
async def on_ready():
    print("Logged in as")
    print(nezuko.user.name)
    print(nezuko.user.id)
    initialization()

nezuko.run(TOKEN)
