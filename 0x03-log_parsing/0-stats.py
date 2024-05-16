#!/usr/bin/python3
"""
Log parser module
"""
import sys
from datetime import datetime
import re
import signal
from time import sleep


line_count = 0
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def check_format(mylist: list) -> bool:
    """ checks if the format is as required"""

    ip = mylist[0]
    time = mylist[2].strip("[]")
    status_code = mylist[-2]
    file_size = mylist[-1]

    regex_pattern = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.' \
                    r'){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
    if bool(re.match(regex_pattern, ip)):

        try:
            datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
            int(status_code)
            int(file_size)

            return True

        except ValueError:
            return False
    else:
        return False


def print_stats(size: int, status_codes: dict):
    """ prints the required stats"""

    print(f"File size: {size}")
    for status_code in status_codes:
        if status_codes[status_code] != 0:
            print(f"{status_code}: {status_codes[status_code]}")


try:
    for line in sys.stdin:
        line_count += 1
        line.strip()
        parts = line.split()
        parts[2:4] = [' '.join(parts[2:4])]
        if not check_format(parts):
            continue

        ip = parts[0]
        time = parts[2].strip("[]")
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_file_size += file_size

        if (status_code in status_codes):
            status_codes[status_code] += 1
        else:
            continue
        if line_count % 10 == 0:
            print_stats(total_file_size, status_codes)
except KeyboardInterrupt:
    try:
        print_stats(total_file_size, status_codes)
    except KeyboardInterrupt:
        pass
    raise
