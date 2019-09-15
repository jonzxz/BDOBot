import datetime as dt
from Time import Time
import math

time = dt.datetime.now().time()

def get_token():
    try:
        with open('token.txt', 'r') as token_file:
            token = token_file.read()
        return token
    except FileNotFoundError:
        print("TOKEN NOT FOUND")

def nextboss():
    # Day of week = 0 - 6
    dayofweek = dt.datetime.today().weekday()

    # Time now
    timenow = dt.datetime.now().time()
    boss=''
    bosstime=''
    today = dayofweek
    is_found = False
    try:
        for i, value in enumerate(week[today]):
            if timenow < value.get_time():
                is_found = True
                boss = week[today][i].get_name()
                bosstime = (week[today][i].get_time()).strftime('%H:%M')
                break
        if is_found == False:
            boss = week[today+1][0].get_name()
            bosstime = (week[today+1][0].get_time()).strftime('%H:%M')

    except KeyError:
        boss = week[0][0].get_name()
        bosstime = (week[0][0].get_time()).strftime('%H:%M')

    return 'The next boss is ' + boss + ' at ' + bosstime + 'hrs, GMT+8'

def mpcheck(silver):
    return 'Without VP : ' + str(math.floor(float(silver)*0.65)) + '\nWith VP\t: ' + str(math.floor(float(silver)*0.845))


FAILSTACK = 'For Boss Armors/Weapons\n' \
            'PRI: 16-20\n' \
            'DUO: 21-30\n' \
            'TRI: 30-44\n' \
            'TET: 45 - 100\n' \
            'PEN: 100+\n\n' \
            'For Yellow Accessories\n' \
            'PRI: 18\n' \
            'DUO: 40\n' \
            'TRI: 44\n' \
            'TET: 80+\n' \
            'PEN: 120+\n'

week = {
    0: [ #MONDAY
        Time(time.replace(hour=1, minute=30, second=0), 'Kzarka'),
        Time(time.replace(hour=7, minute=0, second=0), 'Garmoth'),
        Time(time.replace(hour=15, minute=0, second=0), 'Nouver'),
        Time(time.replace(hour=16, minute=0, second=0), 'Karanda'),
        Time(time.replace(hour=20, minute=0, second=0), 'Kzarka'),
        Time(time.replace(hour=23, minute=59, second=59), 'Offin')
    ],
    1: [ #TUESDAY
        Time(time.replace(hour=1, minute=30, second=0), 'Nouver'),
        Time(time.replace(hour=7, minute=0, second=0), 'Kutum'),
        Time(time.replace(hour=11, minute=0, second=0), 'Kzarka'),
        Time(time.replace(hour=15, minute=0, second=0), 'Kutum'),
        Time(time.replace(hour=16, minute=0, second=0), 'Nouver'),
        Time(time.replace(hour=20, minute=0, second=0), ['Muraka', 'Quint']),
        Time(time.replace(hour=23, minute=59, second=59), ['Kutum', 'Nouver'])
    ],
    2: [ #WEDNESDAY
        Time(time.replace(hour=1, minute=30, second=0), 'Kzarka'),
        Time(time.replace(hour=11, minute=0, second=0), 'Kzarka'),
        Time(time.replace(hour=15, minute=0, second=0), 'Karanda'),
        Time(time.replace(hour=20, minute=0, second=0), 'Kutum'),
        Time(time.replace(hour=23, minute=59, second=59), 'Offin')
    ],
    3: [ #THURSDAY
        Time(time.replace(hour=1, minute=30, second=0), 'Kutum'),
        Time(time.replace(hour=7, minute=0, second=0), 'Nouver'),
        Time(time.replace(hour=11, minute=0, second=0), 'Kzarka'),
        Time(time.replace(hour=15, minute=0, second=0), 'Kutum'),
        Time(time.replace(hour=16, minute=0, second=0), ['Kzarka', 'Karanda']),
        Time(time.replace(hour=20, minute=0, second=0), 'Garmoth'),
        Time(time.replace(hour=23, minute=59, second=59), ['Kzarka', 'Nouver'])
    ],
    4: [ #FRIDAY
        Time(time.replace(hour=1, minute=30, second=0), 'Kzarka'),
        Time(time.replace(hour=7, minute=0, second=0), 'Karanda'),
        Time(time.replace(hour=11, minute=0, second=0), 'Kutum'),
        Time(time.replace(hour=15, minute=0, second=0), 'Kzarka'),
        Time(time.replace(hour=20, minute=0, second=0), 'Nouver'),
        Time(time.replace(hour=23, minute=59, second=59), 'Offin')
    ],
    5: [ #SATURDAY
        Time(time.replace(hour=1, minute=30, second=0), 'Karanda'),
        Time(time.replace(hour=7, minute=0, second=0), 'Nouver'),
        Time(time.replace(hour=11, minute=0, second=0), ['Kutum', 'Kzarka']),
        Time(time.replace(hour=15, minute=0, second=0), ['Karanda', 'Nouver']),
        Time(time.replace(hour=16, minute=0, second=0), 'Garmoth'),
        Time(time.replace(hour=20, minute=0, second=0), ['Muraka', 'Quint'])
    ],
    6: [ #SUNDAY
        Time(time.replace(hour=1, minute=30, second=0), 'Karanda'),
        Time(time.replace(hour=7, minute=0, second=0), 'Kutum'),
        Time(time.replace(hour=11, minute=0, second=0), ['Karanda', 'Kzarka']),
        Time(time.replace(hour=15, minute=0, second=0), ['Kutum', 'Nouver']),
        Time(time.replace(hour=16, minute=0, second=0), 'Vell'),
        Time(time.replace(hour=20, minute=0, second=0), 'Karanda'),
        Time(time.replace(hour=23, minute=59, second=59), ['Kutum', 'Nouver'])
    ]
}