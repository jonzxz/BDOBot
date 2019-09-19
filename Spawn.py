from datetime import time

"""
The Spawn class contains a datetime.time and a string/list name.
The class represents a point in time where a boss will spawn.
As there are times where 2 bosses will spawn at the same time, name
might be a list, thus the check in get_name
"""


class Spawn:
    def __init__(self, spawn_time: time, name):
        self.spawn_time = spawn_time
        self.name = name

    def get_name(self):
        if type(self.name) is list:
            return ' & '.join(self.name)
        return self.name

    def set_name(self, name):
        self.name = name

    def get_time(self):
        return self.spawn_time

    def set_time(self, spawn_time):
        self.spawn_time = spawn_time
