from data import week
import datetime as dt
import os
from Logger import logger

"""
utils contains individual functions that kind of do not fit anywhere(yet)
it is not completely tidied up so things here are a little messy.
"""


# a and b makes the time object into datetime objects so they can be delta-ed
# the condition is to test if current time int vs. next boss time int in hrs is larger
# if it is then it represents that a day have passed, thus a day+1 delta is added

def time_diff(next_boss_time):
    time_now = dt.datetime.now().time()
    a = dt.datetime.combine(dt.date.today(), time_now)
    b = dt.datetime.combine(dt.date.today(), next_boss_time)
    if int(a.hour - b.hour) > 0:
        b = dt.datetime.combine(dt.date.today() + dt.timedelta(days=1), next_boss_time)
    delta = b - a
    # print(delta.seconds)
    return delta.seconds.real


def get_token():
    logger.info("get_token() invoked")
    DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

    if not (DISCORD_TOKEN):
        logger.warning('DISCORD_TOKEN env var not found, attempting to read token.txt')
        try:
            with open('token.txt', 'r') as token_file:
                token = token_file.read()
                token_file.close()
                DISCORD_TOKEN = token
        except FileNotFoundError:
            logger.error("token.txt not found")
    return DISCORD_TOKEN

def get_global_configs():
    logger.info("initializing global configs")
    OWNER_ID = 382152478810046464 # Jon
    # SERVER_ID = 620980624525754399 #TESTBED
    SERVER_ID = 574641536214630401 # Pastries
    return [OWNER_ID, SERVER_ID]

def get_startup_modules():
    logger.info("initializing startup modules")
    MODULES_GENERAL = 'Modules.General'
    MODULES_MARKET = 'Modules.Market'
    MODULES_BOSS = 'Modules.Boss'
    MODULES_FUN = 'Modules.Fun'

    return [MODULES_GENERAL, MODULES_MARKET, MODULES_BOSS, MODULES_FUN]

def get_praw_secrets():
    logger.info("retrieving PRAW ID and secret")
    CLIENT_ID = os.environ.get('PRAW_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('PRAW_CLIENT_SECRET')

    if not (CLIENT_ID or CLIENT_SECRET):
        logger.warning("PRAW env vars not found, attempting to read praw_secrets.txt")
        try:
            with open('praw_secrets.txt', 'r') as praw_secrets:
                secrets = praw_secrets.read().split(sep='\n')
                praw_secrets.close()
                PRAW_SECRETS = [secrets[0], secrets[1]]
        except FileNotFoundError:
            logger.error("praw_secrets.txt not found")
            logger.error("REDDIT MODULE NOT STARTED")
    else:
        PRAW_SECRETS = [CLIENT_ID, CLIENT_SECRET]
    return PRAW_SECRETS

# this function takes the current day and time and compare against the dict of Spawns
# from data.weeks to retrieve the next Spawn by closest time from now and returns a Spawn object
def next_boss():
    # Day of week = 0 - 6
    day_of_week = dt.datetime.today().weekday()
    # Time now
    time_now = dt.datetime.now().time()
    today = day_of_week
    is_found = False
    try:
        for i, value in enumerate(week[today]):
            if time_now < value.get_time():
                is_found = True
                boss = week[today][i]
                break
        if is_found is False:
            boss = week[today+1][0]

    except KeyError:
        boss = week[0][0]

    return boss
