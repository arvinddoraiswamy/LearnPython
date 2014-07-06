"""
- Can call a custom function while using list comprehensions.
"""

def main():
    enc_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq\
    ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm\
    jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    split_enc_string = list(enc_string)
    dec_string = [ decrypt(char) for char in split_enc_string ]

    print ''.join(dec_string)

def decrypt(char):
    if 97 <= ord(char) <= 120:
        return chr(ord(char) + 2)
    elif ord(char) == 121:
        return 'a'
    elif ord(char) == 122:
        return 'b'
    else:
        return char

if __name__ == "__main__":
    main()
