from discord.ext import commands
import praw, random

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


def setup(bot):
    bot.add_cog(Fun(bot))
