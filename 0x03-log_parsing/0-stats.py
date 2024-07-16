#!/usr/bin/python3


import sys
import signal


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)


def main():
    line_count = 0
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                size = int(parts[-1])
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
                total_size += size
            except Exception:
                pass

            line_count += 1
            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        signal.signal(signal.SIGINT, signal_handler)
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
