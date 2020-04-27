#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Loreto Parisi (loretoparisi at gmail dot com)
# Code: https://github.com/loretoparisi/contacttracing
# adapted from: https://github.com/gretelai/contact-tracing-experiment
#

try:
    from .life import Life
except:
    from life import Life

import json
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

def print_time(ts):
    value = datetime.datetime.utcfromtimestamp(ts)
    print( value.strftime('%Y-%m-%d %H:%M:%S') )

def download_report(fname):
      # LP: it works in notebook only
      import ipywidgets as widgets
      from IPython.display import display
      button = widgets.Button(description="Download Report")
      output = widgets.Output()

      def on_button_clicked(b):
        # Display the message within the output widget.
        with output:
          from google.colab import files
          files.download(fname)

      button.on_click(on_button_clicked)
      display(button, output)

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
    report = life.generate_report()
    report = json.loads( report )
    print( report )