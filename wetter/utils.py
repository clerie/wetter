#!/usr/bin/env python3

from datetime import datetime

def fromisoformat(str):
    return datetime.strptime(str, '%Y-%m-%d').date()
