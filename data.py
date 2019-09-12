import datetime


FAILSTACK = 'For Boss Armors/Weapons\n' \
            'PRI: 16-20\n' \
            'DUO: 21-30\n' \
            'TRI: 30-44\n' \
            'TET: 45 - 100\n' \
            'PEN: idk bro\n\n' \
            'For Yellow Accessories\n' \
            'PRI: 18\n' \
            'DUO: 40\n' \
            'TRI: 44\n' \
            'TET: 80+\n' \
            'PEN: idk bro\n'

def getday():
    return str(datetime.datetime.today().weekday())
