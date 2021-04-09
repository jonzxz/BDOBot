from Spawn import Spawn
import datetime as dt

"""
This file contains data that will be used by other classes/functions
week - contains Spawn data for the week with the keys being days of week
failstack - still a work in progress, to be redone
"""

week = {
    0: [ #MONDAY
        Spawn(dt.time(hour=1, minute=30, second=0), 'Kutum'),
        Spawn(dt.time(hour=11, minute=0, second=0), ['Kzarka', 'Nouver']),
        Spawn(dt.time(hour=15, minute=0, second=0), ['Kutum', 'Nouver']),
        Spawn(dt.time(hour=20, minute=0, second=0), ['Karanda', 'Kzarka']),
        Spawn(dt.time(hour=23, minute=59, second=59), 'Offin')
    ],
    1: [ #TUESDAY
        Spawn(dt.time(hour=1, minute=30, second=0), 'Nouver'),
        Spawn(dt.time(hour=11, minute=0, second=0), ['Karanda', 'Kutum']),
        Spawn(dt.time(hour=15, minute=0, second=0), ['Kutum', 'Kzarka']),
        Spawn(dt.time(hour=20, minute=0, second=0), ['Muraka', 'Quint']),
        Spawn(dt.time(hour=23, minute=59, second=59), 'Garmoth')
    ],
    2: [ #WEDNESDAY
        Spawn(dt.time(hour=1, minute=30, second=0), ['Kzarka', 'Offin']),
        Spawn(dt.time(hour=11, minute=0, second=0), ['Nouver', 'Kutum']),
        Spawn(dt.time(hour=15, minute=0, second=0), ['Karanda', 'Kzarka']),
        Spawn(dt.time(hour=20, minute=0, second=0), ['Kutum', 'Nouver']),
        Spawn(dt.time(hour=23, minute=59, second=59), 'Vell')
    ],
    3: [ #THURSDAY
        Spawn(dt.time(hour=1, minute=30, second=0), 'Kutum'),
        Spawn(dt.time(hour=11, minute=0, second=0), ['Karanda', 'Kzarka']),
        Spawn(dt.time(hour=15, minute=0, second=0), ['Kutum', 'Nouver']),
        Spawn(dt.time(hour=20, minute=0, second=0), ['Karanda', 'Nouver']),
        Spawn(dt.time(hour=23, minute=59, second=59), 'Garmoth')
    ],
    4: [ #FRIDAY
        Spawn(dt.time(hour=1, minute=30, second=0), 'Nouver'),
        Spawn(dt.time(hour=11, minute=0, second=0), ['Kutum', 'Kzarka']),
        Spawn(dt.time(hour=15, minute=0, second=0), ['Karanda', 'Kzarka']),
        Spawn(dt.time(hour=20, minute=0, second=0), ['Kutum', 'Nouver']),
        Spawn(dt.time(hour=23, minute=59, second=59), 'Offin')
    ],
    5: [ #SATURDAY
        Spawn(dt.time(hour=1, minute=30, second=0), 'Karanda'),
        Spawn(dt.time(hour=11, minute=0, second=0), ['Kutum', 'Kzarka']),
        Spawn(dt.time(hour=15, minute=0, second=0), ['Karanda', 'Nouver']),
        Spawn(dt.time(hour=16, minute=0, second=0), 'Garmoth'),
        Spawn(dt.time(hour=20, minute=0, second=0), ['Muraka', 'Quint'])
    ],
    6: [ #SUNDAY
        Spawn(dt.time(hour=1, minute=30, second=0), 'Kzarka'),
        Spawn(dt.time(hour=11, minute=0, second=0), ['Karanda', 'Nouver']),
        Spawn(dt.time(hour=15, minute=0, second=0), ['Karanda', 'Kutum']),
        Spawn(dt.time(hour=16, minute=0, second=0), 'Vell'),
        Spawn(dt.time(hour=20, minute=0, second=0), ['Karanda', 'Kzarka']),
        Spawn(dt.time(hour=23, minute=59, second=59), ['Kutum', 'Nouver'])
    ]
}

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
