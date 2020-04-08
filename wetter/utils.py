#!/usr/bin/env python3

from datetime import datetime

def fromisoformat(str):
    return datetime.strptime(str, '%Y-%m-%d').date()

def toisoformat(str, alt=""):
    try:
        return fromisoformat(str).isoformat()
    except:
        return alt
