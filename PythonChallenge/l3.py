"""
- Using ^ at the start of a character class inverts it.

- Using groups inside the search pattern and then using findall() prints only
that group.
"""
import re

def main():
    filename = 'l3_text'
    with open(filename, 'rU') as f:
        string = f.read()

    search_for_pattern(string)

def search_for_pattern(string):
    pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
    regex = re.compile(pattern)
    match = regex.findall(string)
    print ''.join(match)

if __name__ == "__main__":
    main()
