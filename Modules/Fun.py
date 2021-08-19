from discord.ext import commands
import asyncpraw, random, requests, re, Constants, os
from bs4 import BeautifulSoup
from mal import Anime, AnimeSearch, Manga, MangaSearch
from utils import get_praw_secrets
from Logger import logger
from discord.utils import get

class Fun(commands.Cog):
    def __init__(self, bot):
        logger.info(Constants.COG_STARTUP, Constants.FUN)
        self.bot = bot
        # Reddit API id and secret is stored within my PRAW's praw.ini as [nezuko] entry.
        praw_secrets = get_praw_secrets()
        self.reddit = asyncpraw.Reddit(user_agent=Constants.NEZUKO_BOT, client_id=praw_secrets[0], client_secret=praw_secrets[1])
        self.subreddits = Constants.MEME_SUBREDDITS
        self.uwu_subreddits = Constants.UWU_SUBREDDITS

    @commands.command(name=Constants.MEME_L)
    async def get_meme(self, ctx):
        sub_to_pick = random.randint(Constants.ZERO, Constants.TWO)
        post_to_pick = random.randint(Constants.ONE, Constants.TEN)
        subreddit_chosen = await self.reddit.subreddit(self.subreddits[sub_to_pick])
        chosen_submissions = [sub async for sub in subreddit_chosen.hot(limit=15) if not sub.stickied]
        chosen_submission = chosen_submissions[post_to_pick]
        await ctx.send(chosen_submission.url)

    @commands.command(name=Constants.UWU_L)
    async def get_uwu(self, ctx):
        post_to_pick = random.randint(Constants.ONE, Constants.TEN)
        subreddit_chosen = await self.reddit.subreddit(self.uwu_subreddits[0])
        chosen_submissions = [sub async for sub in subreddit_chosen.hot(limit=15) if not sub.stickied]
        chosen_submission = chosen_submissions[post_to_pick]
        await ctx.send(chosen_submission.url)

    @commands.command(name=Constants.ANIME_L)
    async def get_anime(self, ctx, *args):
        logger.info(Constants.FUN_QUERY_SENT, Constants.ANIME, " ".join(args))
        try:
            anime_search = AnimeSearch(" ".join(args))
            anime = Anime((anime_search.results[0]).mal_id)
            await ctx.send(Constants.MSG_FUN_RESPONSE.format(anime.title, anime.synopsis, anime.image_url))
        except Exception:
            logger.error(Constants.FUN_QUERY_ERR, Constants.ANIME, ' '.join(args))
            await ctx.send(Constants.MSG_FUN_ERR.format(Constants.ANIME, ' '.join(args)))

    @commands.command(name=Constants.MANGA_L)
    async def get_manga(self, ctx, *args):
        logger.info(Constants.FUN_QUERY_SENT, Constants.MANGA, " ".join(args))
        try:
            manga_search = MangaSearch(" ".join(args))
            manga = Manga((manga_search.results[0]).mal_id)
            await ctx.send(Constants.MSG_FUN_RESPONSE.format(manga.title, manga.synopsis, manga.image_url))
        except Exception:
            logger.error(Constants.FUN_QUERY_ERR, Constants.MANGA, ' '.join(args))
            await ctx.send(Constants.MSG_FUN_ERR.format(Constants.MANGA, ' '.join(args)))

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
    bot.add_cog(Fun(bot))
