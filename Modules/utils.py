from data import week
import datetime as dt

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
    print(delta.seconds)
    return delta.seconds.real


def get_token():
    try:
        with open('token.txt', 'r') as token_file:
            token = token_file.read()
        return token
    except FileNotFoundError:
        print("TOKEN NOT FOUND")


# this function takes the current day and time and compare against the dict of Spawns
# from data.weeks to retrieve the next Spawn by closest time from now and returns a Spawn object
def next_boss():
    # Day of week = 0 - 6
    dayofweek = dt.datetime.today().weekday()
    # Time now
    time_now = dt.datetime.now().time()
    today = dayofweek
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



