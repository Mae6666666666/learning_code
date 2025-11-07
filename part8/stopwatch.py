

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    def __str__(self):
        return f'{self.minutes}: {self.seconds}'

    def tick(self):
            self.seconds += 1
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0
            if self.minutes == 59 and self.seconds == 59:
                self.minutes = 0
                self.seconds = 0




watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()




