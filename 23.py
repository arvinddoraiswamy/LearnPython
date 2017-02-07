import subprocess
from subprocess import Popen, PIPE

#If you just want to run something and do not care about the output, use this
print 'Use check_call if you just want to run something'
print 'Nothing will ever be displayed'
print '-' * 10
subprocess.check_call(["rm", "-rf", "/tmp/out"])

#If you want to do something with the output of a shell command use this
print 'Use check_output to display output'
output= subprocess.check_output(["ls", "-la", "/tmp"])
print output
print '-' * 10

#Pipe output of one command to another
print 'Trying to pipe output of one command to another'
try:
    #Command 1
    ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)

    #Pipe to Command 2
    output = subprocess.check_output(('grep', 'init'), stdin=ps.stdout)
    ps.communicate()
    print output
except subprocess.CalledProcessError:
    print 'No such process found'
print '-' * 10

#http://sam.nipl.net/code/python/pipeline.py
print 'Sending a string as input to another process. Result in output file'
input   = "test string"

#Result stored here eventually
outfile = file('outfile.txt','w')

#Last command
p2 = Popen(['sort'],                  stdin=PIPE, stdout=outfile)

#Middle command. Build this first
p1 = Popen(['sed', 's/$/ hi there/'], stdin=PIPE, stdout=p2.stdin)

#This is done to tell the sort command, that it will receive no more input from sed
p2.stdin.close()

#Strings you are passing to the middle command. This is what you'd type first at a shell prompt.
p1.communicate(input)
