#!/usr/bin/env python3
"""Prints hours worked this week and hours remaining.

Accepts csv of hours from stdin.
month/day, start, end

"""

from __future__ import print_function

import sys
from datetime import datetime

# The number of hours you want to work in a given week.
TARGET_HOURS_PER_WEEK = 35.0

THIS_YEAR = datetime.today().year


def parse_time(time):
    if ":" in time:
        return datetime.strptime(time, "%H:%M")
    else:
        return datetime.strptime(time, "%H")


if len(sys.argv) != 2:
    print("time_this_week.py <hours.csv>")
    sys.exit(1)

# Get today's day and month
this_week = datetime.now().isocalendar()[1]

total_minutes = 0
with open(sys.argv[1]) as input_file:
    # Skip the header row in the file.
    input_file.readline()

    for line in input_file:
        data = line.strip().split(",")
        if len(data) != 3:
            # Ensure valid data.
            continue

        date_str, start, end = data

        # Parse date
        month, day = date_str.split("/")
        date = datetime(THIS_YEAR, int(month), int(day))
        if date.isocalendar()[1] != this_week:
            # Skip data not from this work week.
            continue

        minutes = (parse_time(end) - parse_time(start)).total_seconds() / 60.0
        total_minutes += minutes

hours_worked = total_minutes / 60.0
percent_worked = (hours_worked / TARGET_HOURS_PER_WEEK) * 100

print("%1.2f hours worked this week. (%d%%)" % (hours_worked, percent_worked))
print("%1.2f hours remaining." % (TARGET_HOURS_PER_WEEK - hours_worked))
