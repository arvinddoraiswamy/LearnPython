"""
Usage of the Python requests module. urllib and httplib are more famous, but I
found requests much much easier to use.

Used the parentheses to get what we need from findall(). Same as previous
solution.

Responses give different patterns and we need to follow the numbers in each
response. The 250th request gives out a HTML file - peak.html. Unless you knew
the format of the answer before itself, you can't make it STOP when you reach
it. It will however, exit after the loop counter reaches 400, so it's still OK.
"""

import requests
import re

def main():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
    r1 = requests.get(url)
    next_nothing = r1.content.split()[5]

    pattern = r'.*and the next nothing is (\d+)'
    regex = re.compile(pattern)

    for count in range(400):
        r2 = requests.get(url+str(next_nothing))
        match = regex.findall(r2.content)
        if match:
            next_nothing = match[0]
        else:
            next_nothing = int(next_nothing,10)/2
            print str(count)+"\t"+str(r2.content)+"\t"+str(match)

if __name__ == "__main__":
    main()
