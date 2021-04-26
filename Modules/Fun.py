from discord.ext import commands
import praw, random, requests, re
from bs4 import BeautifulSoup
from mal import Anime, AnimeSearch, Manga, MangaSearch
from utils import get_praw_secrets
import os
from Logger import logger
from discord.utils import get

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Reddit API id and secret is stored within my PRAW's praw.ini as [nezuko] entry.
        praw_secrets = get_praw_secrets()
        self.reddit = praw.Reddit(user_agent='NezukoBot', client_id=praw_secrets[0], client_secret=praw_secrets[1])
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
    async def get_anime(self, ctx, *args):
        logger.info("anime name: %s passed in", " ".join(args))
        try:
            anime_search = AnimeSearch(" ".join(args))
            anime = Anime((anime_search.results[0]).mal_id)
            await ctx.send('```{0}```\n```{1}```\n{2}'.format(anime.title, anime.synopsis, anime.image_url))
        except Exception:
            logger.error("unable to retrieve anime name: %s", ' '.join(args))
            await ctx.send('An error occured while retrieving anime {0} :('.format(' '.join(args)))

    @commands.command(name='manga')
    async def get_manga(self, ctx, *args):
        logger.info("manga name: %s passed in", " ".join(args))
        try:
            manga_search = MangaSearch(" ".join(args))
            manga = Manga((manga_search.results[0]).mal_id)
            await ctx.send('```{0}```\n```{1}```\n{2}'.format(manga.title, manga.synopsis, manga.image_url))
        except Exception:
            logger.error("unable to retrieve manga name: %s", ' '.join(args))
            await ctx.send('An error occured while trieving manga {0} :('.format(' '.join(args)))

    @commands.command(name='popcorn')
    async def set_bh_role(self, message):
        POPCORN_ID = 707958341539856404
        role = get(message.guild.roles, id=POPCORN_ID)
        member = message.author
        chn = message.channel
        if role not in member.roles:
            await member.add_roles(role)
            await chn.send("{0.author.mention} is now registered as a Caramel Popcorn!".format(message))
        elif role in member.roles:
            await member.remove_roles(role)
            await chn.send("{0.author.mention} have resigned as a Caramel Popcorn!".format(message))

def setup(bot):
    bot.add_cog(Fun(bot))
