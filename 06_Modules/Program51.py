# Date Time Module

import datetime

print("Current date and time is :", datetime.datetime.today())
now= datetime.datetime.today()
other =datetime.datetime(2021,2,26,12,10)
print("The difference between current time and other time is :", now-other)
other2=datetime.timedelta(18901,55547,421000)
print("Duration, the difference between two dates or times :", now-other2)
print("The maximum year is :", datetime.MAXYEAR)
print("The minimum year is :", datetime.MINYEAR)
print("The time object is :", datetime.time)
print("The timezone object is :", datetime.timezone)

#timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
'''Only days, seconds and microseconds are stored internally.
Arguments are converted to those units:
A millisecond is converted to 1000 microseconds.
A minute is converted to 60 seconds.
An hour is converted to 3600 seconds.
A week is converted to 7 days.
and days, seconds and microseconds are then normalized
so that the representation is unique, with
0 <= microseconds < 1000000
0 <= seconds < 3600*24 (the number of seconds in one day)
-999999999 <= days <= 999999999'''
