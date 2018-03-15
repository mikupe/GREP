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


#selže přiřazování argumentů
try:
    pattern, path = sys.argv[1:]
except ValueError:
    print(__doc__.strip(), file=sys.stderr)
    sys.exit(1)
    
    
#selže otevírání souborů
try:
    with open(path) as f:
        for line in f:
            if re.search(pattern,line):
                print(line, end="")
except FileNotFoundError:
    print("file not found:", path, file=sys.stderr)
    sys.exit(1)