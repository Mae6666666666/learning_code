

class Clock:

    def __init__(self, hours_temp: int, minutes_temp: int, seconds_temp: int):
        self.hours = hours_temp
        self.minutes = minutes_temp
        self.seconds = seconds_temp


    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0



    def set(self, hours_temp: int = 0, minutes_temp: int = 0, seconds_temp: int = 0):
        self.hours = hours_temp
        self.minutes = minutes_temp
        self.seconds = seconds_temp





clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)