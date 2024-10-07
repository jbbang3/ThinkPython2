import math

class Time:
    """Represent the time of day
    Attributes: hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        assert self.valid_time() and other.valid_time()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def __radd__(self, other):
        return self.__add__(other)

    def printtime(self):
        print('{}:{}:{}'.format(self.hour,self.minute, self.second))

    def time_to_int(self):
        minutes=self.hour*60 +self.minute
        seconds=minutes*60 +self.second
        return seconds
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    
    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True

    def mul_time(self, n):
        assert self.valid_time() and isinstance(n, int)
        ans = n * self.time_to_int()
        return int_to_time(ans)

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def main():
    time = Time(11, 59, 30)
    time2 = Time(1, 59, 30)
    print('wdf')

    print(time+time2)
    time2.mul_time(4).printtime()

    print(hasattr(time, 'hour'))
    print(vars(time))



if __name__=="__main__":
    main()