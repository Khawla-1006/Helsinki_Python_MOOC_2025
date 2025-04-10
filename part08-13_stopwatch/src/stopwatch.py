# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds == 59 :
            self.minutes += 1 
            self.seconds = 0
        else :
            self.seconds += 1
        if self.minutes > 59 :
            self.minutes = 0
    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(60*59+59):
        print(watch)
        watch.tick()