import hashlib

message='test teddy well'
print 'MD5', hashlib.md5(message).hexdigest()
print 'SHA1', hashlib.sha1(message).hexdigest()
print 'SHA224', hashlib.sha224(message).hexdigest()
print 'SHA256', hashlib.sha256(message).hexdigest()
print 'SHA384', hashlib.sha384(message).hexdigest()
print 'SHA512', hashlib.sha512(message).hexdigest()

print 'PBKDF2 after Python 2.7.9',  hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000, dklen=40)
