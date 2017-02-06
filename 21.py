import os
import sys

def handle_err(e):
    print "Error handling directory"
    print e
    print '-'* 10

print 'System info'
systeminfo= os.uname()
print systeminfo

print 'Environment'
env= os.environ
print env

print 'UID/GID'
euid= os.getresuid()
egid= os.getresgid()
print euid, egid

print 'PID/PPID'
print os.getpid()
print os.getppid()

print 'Files/Directories'
print os.getcwd()
os.chdir('/')
print os.getcwd()
print os.listdir('/data')
print "Creating a file"
f1= open('/tmp/test1', 'w')
print "Deleting file now"
os.unlink('/tmp/test1')

os.mkdir('/tmp/test1')
os.stat('/tmp/test1')
os.rmdir('/tmp/test1')

print 'Walking through a directory tree'
for root, dirs, files in os.walk('/tmp', onerror=handle_err):
    print 'Each dir ', root
    print 'Dir inside each root dir', dirs
    print 'Files inside each root dir', files
    print '-' * 10

print '10 random bytes', os.urandom(10)

print 'Executing a command quickly', os.system('/bin/pwd>/tmp/out')
print 'Using execl', os.execl('/bin/ls', ' ', '-l', '/etc/')
