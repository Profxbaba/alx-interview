#!/usr/bin/python3

import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    global total_size, status_codes
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_count = 0

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) >= 9:
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        if status_code in status_codes:
            status_codes[status_code] += 1
            total_size += file_size
            line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0

print_stats()
