from data import week
import os, Constants, asyncio, datetime as dt
from Logger import logger
from discord.message import Message
from typing import List
from discord.role import Role

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
    logger.info(Constants.RETRIEVE_DISCORD_CONFIG)
    DISCORD_TOKEN = os.environ.get(Constants.DISCORD_TOKEN)
    if not (DISCORD_TOKEN):
        logger.warning(Constants.ENV_VAR_NOT_FOUND, Constants.DISCORD_TOKEN, Constants.DOTENV_FILE)
        try:
            with open(Constants.DOTENV_FILE, Constants.FILE_READ_MODE) as token_file:
                token = token_file.read().split(sep='\n')
                token_file.close()
                DISCORD_TOKEN = token[0].split(sep='=')[1]
                logger.info(Constants.CONFIG_FILE_RETRIEVE_SUCCESS, Constants.DISCORD_TOKEN, Constants.DOTENV_FILE)
        except FileNotFoundError:
            logger.error(Constants.FILE_NOT_FOUND, Constants.DOTENV_FILE)
    return DISCORD_TOKEN

def get_praw_secrets():
    logger.info(Constants.RETRIEVE_PRAW_CONFIG)
    CLIENT_ID = os.environ.get(Constants.PRAW_CLIENT_ID)
    CLIENT_SECRET = os.environ.get(Constants.PRAW_CLIENT_SECRET)

    if not (CLIENT_ID or CLIENT_SECRET):
        logger.warning(Constants.ENV_VAR_NOT_FOUND, Constants.PRAW_CLIENT_ID + '/' + Constants.PRAW_CLIENT_SECRET, Constants.DOTENV_FILE)
        try:
            with open(Constants.DOTENV_FILE, Constants.FILE_READ_MODE) as praw_secrets:
                secrets = praw_secrets.read().split(sep='\n')
                praw_secrets.close()
                PRAW_SECRETS = [secrets[1].split(sep='=')[1], secrets[2].split(sep='=')[1]]
                logger.info(Constants.CONFIG_FILE_RETRIEVE_SUCCESS, Constants.PRAW_CLIENT_ID + '/' + Constants.PRAW_CLIENT_SECRET, Constants.DOTENV_FILE)
        except FileNotFoundError:
            logger.error(Constants.FILE_NOT_FOUND, Constants.DOTENV_FILE)
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

async def add_msg_reactions(msg: Message, msg_type: str) -> None:
    if (msg_type == Constants.YES_NO):
        logger.info(Constants.ADD_REACTION_FOR_MSG, Constants.YES_NO)
        await msg.add_reaction(Constants.EMOJI_Y)
        await msg.add_reaction(Constants.EMOJI_N)
    if (msg_type == Constants.UPDATE):
        logger.info(Constants.ADD_REACTION_FOR_MSG, Constants.UPDATE)
        await msg.add_reaction(Constants.EMOJI_STATUS)
        await msg.add_reaction(Constants.EMOJI_OPEN)
        await msg.add_reaction(Constants.EMOJI_CLOSE)
    if (msg_type == Constants.ROLES_UPDATE_COMD):
        logger.info(Constants.ADD_REACTION_FOR_MSG, Constants.ROLES_UPDATE_COMD)
        await msg.add_reaction(Constants.EMOJI_EL_SIP_C)
        await msg.add_reaction(Constants.EMOJI_BAM_MAD_C)
        await msg.add_reaction(Constants.EMOJI_EL_YAY_C)
        await msg.add_reaction(Constants.EMOJI_MIIA_GASP_C)
    if (msg_type == Constants.WAR_CAPS):
        logger.info(Constants.ADD_REACTION_FOR_MSG, Constants.WAR_CAPS)
        await msg.add_reaction(Constants.EMOJI_REGIONAL_S)
        await msg.add_reaction(Constants.EMOJI_REGIONAL_T)
        await msg.add_reaction(Constants.EMOJI_REGIONAL_F)
def is_creme_brulee(role_list: List[Role]) -> bool:
    return Constants.ID_ROLE_CREME in [role.id for role in role_list]

def is_brioche_bun(role_list: List[Role]) -> bool:
    return Constants.ID_ROLE_BRIOCHE in [role.id for role in role_list]

def equals(a, b):
    return a == b
