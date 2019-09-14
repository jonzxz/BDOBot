class Day:
    def __init__(self, day, name):
        self.day = day
        self.name = name
        self.arr_of_timings = []

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def get_timings(self):
        return self.arr_of_timings

    def set_timings(self, arr):
        self.arr_of_timings = arr

    def get_name(self):
        return self.name