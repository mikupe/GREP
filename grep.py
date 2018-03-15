#!/usr/bin/env python3
'''Usage: grep.py PATTERN FILE...

Search for lines containing PATTERN in FILE(s).
PATTERN can be a regex.

'''

import sys
#selže import

try:
    import regex as re
except ModuleNotFoundError:
    print(
        "regex not module not found, you are currently using re module",
        file=sys.stderr)
    import re

#hodit do fce
#selže přiřazování argumentů


def parse_argv(argv):
    pattern, paths = argv[0], argv[1:]
    if len(paths) < 2:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)
    return argv[0], argv[1:]


#hodit do fce
#selže otevírání souborů


def grep(file):
    for line in file:
        if re.search(pattern, line):
            print(line, end="")


def main(argv):
    pattern, path = parse_argv(argv)
    for path in paths:
        try:
            with open(path) as f:
                grep(file)
        except FileNotFoundError:
            print("file not found:", path, file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
