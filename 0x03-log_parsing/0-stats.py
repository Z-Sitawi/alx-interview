#!/usr/bin/python3

import sys
import re


def print_message(dict_sc, total_file_size):
    """
    Function to print statistics
    Args:
        dict_sc: Dictionary of status codes and their counts
        total_file_size: Total accumulated file size
    """
    print(f'Total file size: {total_file_size}')
    for code in sorted(dict_sc.keys()):
        if dict_sc[code] > 0:
            print(f'{code}: {dict_sc[code]}')


total_file_size = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(r'^\S+ \S+ \S+ \[(.*?)] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)
        if match:
            status_code = match.group(2)
            file_size = int(match.group(3))

            total_file_size += file_size

            if status_code in dict_sc:
                dict_sc[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_message(dict_sc, total_file_size)
                print()  # Print an empty line for separation

except KeyboardInterrupt:
    # If interrupted, print the final accumulated statistics
    print_message(dict_sc, total_file_size)
