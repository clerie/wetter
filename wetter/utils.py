#!/usr/bin/env python3

from datetime import datetime, timedelta

def fromisoformat(str):
    return datetime.strptime(str, '%Y-%m-%d').date()

def toisoformat(str, alt=""):
    try:
        return fromisoformat(str).isoformat()
    except:
        return alt

def daterangeofdays(fr, to):
    return [fr + timedelta(days=x) for x in range(0, (to - fr).days + 1)]

def daterangefilterweekend(dates):
    return [date for date in dates if date.weekday() < 5]

def strtobool(s):
    return str(s).lower() in ['true', '1', 't', 'y', 'yes', 'on']
