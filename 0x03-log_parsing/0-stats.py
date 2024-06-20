#!/usr/bin/python3

import sys


def print_message(statusCodeDict, ttfs):
    """
    Method to print
    Args:
        statusCodeDict: dict of status codes
        ttfs: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(ttfs))
    for key, val in sorted(statusCodeDict.items()):
        if val != 0:
            print("{}: {}".format(key, val))


ttfs = 0
code = 0
counter = 0
statusCodeDict = {"200": 0,
                  "301": 0,
                  "400": 0,
                  "401": 0,
                  "403": 0,
                  "404": 0,
                  "405": 0,
                  "500": 0
                  }

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                ttfs += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if code in statusCodeDict.keys():
                    statusCodeDict[code] += 1

            if counter == 10:
                print_message(statusCodeDict, ttfs)
                counter = 0

finally:
    print_message(statusCodeDict, ttfs)
