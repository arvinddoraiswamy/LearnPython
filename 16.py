import re

pattern= 'test'
string1= 'this is a test or another test2 test3'
string2= 'test is a failure'
string3= 'success=1 and failure != 23'

"""
Search for the first occurence of a pattern in a string
"""
m1= re.search(pattern, string1)
print "First position and occurence of the pattern in the string"
print m1.start(), m1.end(), m1.group()

"""
Check if the string starts with a specific pattern
"""
m1= re.match(pattern, string2)
print "Regex using match()"
print m1.group()

"""
Create a pattern which can be used multiple times. It returns a regex object that can then be used in search() and match()
For anything complex it is probably good to use this instead of match or search. If its very simple matching though, compile isn't needed.
"""
variable= 'failure'
regex=re.compile(r'^(.*?=\d)\s{1}and\s{1}%s\s!=\s{1}\d[23]$'%variable,re.IGNORECASE|re.DOTALL|re.MULTILINE|re.X)
m1=regex.match(string3)
if m1:
    print "Regex using compile()"
    print m1.start(), m1.group()

"""
Split string by regex. This is useful in case you want to split strings using complex patterns. For normal strings the default Python split
call can be used.
"""
l1= []
l1= re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
print "Splitting a string using regex"
print l1

"""
Find all occurences of a pattern in a string
"""
flags= re.IGNORECASE|re.DOTALL
t1= re.findall(pattern, string1, flags) 
print t1

"""
Substitute a pattern in a string with a new pattern
"""
s2= re.sub('test','ball',string1)
print s2

"""
Regex character classes
"""
string4= 'cdddbcdef this bLAH Boo 123 456'
m1= re.search(r'[abcdefghijklmnopqrstuvwxyz]*', string4)
print "Character classes - Any character between a and z, case sensitive, 0 or more times. Sees a non-match, it'll stop immediately."
if m1:
    print m1.group()

string4= 'cdddbcdef this bLAH Boo 123 456'
m1= re.match(r'[a-zA-Z ]*', string4)
print "Character classes - Any character between a and z and space, case in-sensitive, 0 or more times. Sees a non-match, it'll stop immediately."
if m1:
    print m1.group()

m1= re.match(r'[^b]+', string4)
print "Character classes - Negation of the example (Negates 'b' just above). The ^ inside a character class acts as a negation. You CANNOT negate a set though. The moment you hit a non-match though, it'll stop matching immediately."
if m1:
    print m1.group()

string4= 'a+b=c'
m1= re.search(r'[a+]*', string4)
print "Character classes - Match special characters inside a character class. Inside a char class special characters are treated normally Sees a non-match, it'll stop immediately."
if m1:
    print m1.group()

''' Escape string before matching things. Added backslashes in front of special characters. '''
pattern= "(.*)'.*"
s5= "xxx\'bb"
print s5, re.escape(pattern), re.escape(s5)
m1= re.match(pattern, s5)
print 'Escaped match', m1.group(1)

""" Search multiple patterns """
p1 = "\W"
p2 = "\d+"
p3 = "abc.*"

string5 = "abctest"
string4= 'cdddbcdef this bLAH Boo 123 456'
print("search multiple patterns in 1 regex")
print(re.compile("(%s|%s|%s)" % (p1, p2, p3)).findall(string5))
m2 = re.search('test|blah', string4, re.IGNORECASE)
if m2:
    print "Multiple OR patterns"
    print m2.group()
