class Time:
    def __init__(self, timeobj, name):
        self.timeobj = timeobj
        self.name = name

    def get_name(self):
        if type(self.name) is list:
            return ' & '.join(self.name)
        return self.name

    def set_name(self, name):
        self.name = name

    def get_time(self):
        return self.timeobj

    def set_time(self, timeobj):
        self.timeobj = timeobj
