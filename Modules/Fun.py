from discord.ext import commands
import praw, random, requests, re
from bs4 import BeautifulSoup
from mal import Anime

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Reddit API id and secret is stored within my PRAW's praw.ini as [nezuko] entry.
        self.reddit = praw.Reddit('nezuko',
                                  user_agent='NezukoBot')
        self.subreddits = ['memes', 'dank_meme', 'animemes']

    @commands.command(name='meme')
    async def get_meme(self, ctx):
        sub_to_pick = random.randint(0, 2)
        post_to_pick = random.randint(1, 10)
        submissions = self.reddit.subreddit(self.subreddits[sub_to_pick]).hot()
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(name='anime')
    async def get_anime(self, ctx, name):
        h = requests.utils.default_headers()
        h.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })

        url = 'https://myanimelist.net/search/all?q=' + name.replace(' ', '%20')
        r = requests.get(url, headers=h)
        soup = BeautifulSoup(r.content, 'lxml')
        div = soup.find_all("div", {"class": "information di-tc va-t pt4 pl8"})
        a = (div[0].find("a", href=True))
        raw_id = str(a['id'])
        id = (re.split('[^0-9]', raw_id)[-1])

        anime = Anime(id)
        await ctx.send('```{0}```\n```{1}```\n{2}'.format(anime.title, anime.synopsis, anime.image_url))


def setup(bot):
    bot.add_cog(Fun(bot))
