from discord.ext import commands
import praw, random, requests, re
from bs4 import BeautifulSoup
from mal import Anime, AnimeSearch, Manga, MangaSearch
from utils import get_praw_secrets
import os
from Logger import logger

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
        anime_search = AnimeSearch(" ".join(args))
        anime = Anime((anime_search.results[0]).mal_id)
        await ctx.send('```{0}```\n```{1}```\n{2}'.format(anime.title, anime.synopsis, anime.image_url))

    @commands.command(name='manga')
    async def get_manga(self, ctx, *args):
        logger.info("manga name: %s passed in", " ".join(args))
        manga_search = MangaSearch(" ".join(args))
        manga = Manga((manga_search.results[0]).mal_id)
        await ctx.send('```{0}```\n```{1}```\n{2}'.format(manga.title, manga.synopsis, manga.image_url))


def setup(bot):
    bot.add_cog(Fun(bot))
