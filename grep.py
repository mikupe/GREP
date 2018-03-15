#!/usr/bin/env python3

'''Usage: grep.py PATTERN FILE

Search for lines containing PATTERN in FILE.
PATTERN can be a regex.

'''

import sys
#selže import

try:
    import regex as re
except ModuleNotFoundError:
    print("regex not module not found, you are currently using re module", file=sys.stderr)
    import re

#hodit do fce
#selže přiřazování argumentů



def parse_argv(argv):
    try:
        pattern, path = argv
        return pattern, path
    except ValueError:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)
    
#hodit do fce
#selže otevírání souborů

def main(argv):
    pattern, path = parse_argv(argv)
    try:
        with open(path) as f:
            for line in f:
                if re.search(pattern,line):
                    print(line, end="")
    except FileNotFoundError:
        print("file not found:", path, file=sys.stderr)
        sys.exit(1)
    
if __name__ == "__main__":
    main(sys.argv[1:])