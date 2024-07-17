#!/usr/bin/python3
"""
Log parsing script.
"""

import sys
import signal

# Dictionary to store status codes and their counts
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

total_size = 0  # Total file size accumulator
line_count = 0  # Line count accumulator

def print_stats():
    """Print current statistics."""
    global total_size
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Signal handler for SIGINT (Ctrl+C)."""
    print_stats()
    sys.exit(0)

def main():
    global line_count, total_size

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        try:
            parts = line.split()
            ip_address = parts[0]
            date = parts[3].strip('[]')
            request = parts[5].strip('"')
            status_code = parts[8]
            file_size = int(parts[9])

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += file_size
            line_count += 1

            if line_count == 10:
                print_stats()
                line_count = 0

        except Exception:
            continue

    print_stats()

if __name__ == "__main__":
    main()

