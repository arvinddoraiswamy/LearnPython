import struct

''' Refer to docs for all the exact formats. There are many so check them out before converting things yourself '''
''' If there's a specific offset you want to do things from, use pack_into and unack_into from the docs '''

#Integer to string
i1= 1234
print "Int to string as 8 byte little endian", repr(struct.pack("<Q",i1))
print "Int to string as 8 byte big endian", repr(struct.pack(">Q",i1))

#String to integer. Make sure size of destination matches the length of the string
s1= '1234'
print "String to 4 byte integer little endian", struct.unpack("<i", s1)
print "String to 4 byte integer big endian", struct.unpack(">i", s1)

''' Whenever you want to convert to and from binary, think of binascii '''
import binascii
h1= binascii.b2a_hex(s1)
print "String to hex", h1
uh1= binascii.a2b_hex(h1)
print "Hex to string, even a binary string", uh1
