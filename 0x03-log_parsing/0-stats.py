#!/usr/bin/python3
""" module doc here """
import sys
import re
from collections import defaultdict

# Regular expression to match the required log line format
LOG_PATTERN = (r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] '
               r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

# Status codes we are interested in
STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Variables to track statistics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        # Using regular expression to match and extract fields
        match = re.match(LOG_PATTERN, line)
        if match:
            ip_address = match.group(1)
            status_code = match.group(3)
            file_size = int(match.group(4))

            # Update total file size
            total_file_size += file_size

            # Update status code counts
            if status_code in STATUS_CODES:
                status_code_counts[status_code] += 1

            line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: {total_file_size}')
            # Print status code counts sorted by status code
            for code in sorted(STATUS_CODES):
                if status_code_counts[code] > 0:
                    print(f'{code}: {status_code_counts[code]}')
            print('')

except KeyboardInterrupt:
    # If interrupted, print the final accumulated statistics
    print(f'\nFinal statistics:')
    print(f'Total file size: {total_file_size}')
    for code in sorted(STATUS_CODES):
        if status_code_counts[code] > 0:
            print(f'{code}: {status_code_counts[code]}')
    sys.exit(0)
