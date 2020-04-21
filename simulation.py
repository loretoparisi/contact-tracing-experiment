try:
    from .life import Life
except:
    from life import Life

import time
import datetime
from pytz import timezone
import calendar
import pytz

def utc_time2datetime(utc_time, tz=None):
    # convert utc time to utc datetime
    utc_datetime = datetime.datetime.fromtimestamp(utc_time)

    # add time zone to utc datetime
    if tz is None:
        tz_datetime = utc_datetime.astimezone(timezone('utc'))
    else:
        tz_datetime = utc_datetime.astimezone(tz)

    return tz_datetime


def datetime2utc_time(datetime):
    # add utc time zone if no time zone is set
    if datetime.tzinfo is None:
        datetime = datetime.replace(tzinfo=timezone('utc'))

    # convert to utc time zone from whatever time zone the datetime is set to
    utc_datetime = datetime.astimezone(timezone('utc')).replace(tzinfo=None)

    # create a time tuple from datetime
    utc_timetuple = utc_datetime.timetuple()

    # create a time element from the tuple an add microseconds
    utc_time = calendar.timegm(utc_timetuple) + datetime.microsecond / 1E6

    return utc_time

if __name__ == '__main__':
    
    # subjects ranges
    family_range = 3
    friends_range = 10
    coworkers_range = 50
    others_range = 10

    # simulation start time
    now = datetime.datetime.now(datetime.timezone.utc)
    year = now.year
    month = 5
    day = 4
    hour = 7

    d = datetime.datetime(now.year, month, day, hour, 0, 0)
    ts = datetime2utc_time(d)
    
    print("start time:", ts, datetime.datetime.utcfromtimestamp(ts).isoformat())

    life = Life(ts, family_range, friends_range, coworkers_range, others_range)

    # start simulation
    life.start()

    # generate report and download
    life.generate_report()