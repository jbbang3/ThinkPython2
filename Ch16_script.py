from Ch16_time import Time
import Ch16_time as ch
from datetime import date

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 1
time2.minute = 59
time2.second = 30
print('wdf')
time2.printtime()

ch.printtime(ch.add_time(time,time2))
ch.printtime(ch.mul_time(time,4))


def print_day(d):
    ref={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday', 6:'Sunday'}
    print(ref[date.weekday(d)])


##date time module
today = date.today()
print(today)
print_day(today)