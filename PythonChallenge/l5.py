"""
Usage of pickle, a Python serialization module. Here we had to deserialize the
text and then parse the data structure which was ASCII Art.

My initial solution was quite terrible as shown in the comment below. I was searching on how to
do it with list comprehensions and found this in the actual solution posted on
the Wiki.

The cool thing is Python doesn't require you to use those awful two
dimensional arrays like I was *cough* doing.

Things to fix:
- Close open file handle.
"""

import pickle

def main():
    filename = 'l5_banner.p'
    unpickled_data = pickle.load(open(filename, 'rb'))

    string = ""

    for lists in unpickled_data:
        #print lists
        string = [character * count for character, count in lists]
        print ''.join(string)
#        for count in range(len(lists)):
#            string += lists[count][0] * lists[count][1]
#        print string
#        string = ""
#
if __name__ == "__main__":
    main()
