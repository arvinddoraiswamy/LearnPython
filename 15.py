import sys
try:
    x = int('aa')
    print "This isn't printed if a ValueError is thrown"
except ValueError:
    print sys.exc_info()[1]

print "1. This prints even if the exception is thrown"

try:
    x = int('WOOT')
    print "This isn't printed if a ValueError is thrown"
except ValueError:
    print sys.exc_info()[1]
finally:
    print "Finally - This runs even if there is an exception"

try:
    x=[]
    x.append(int(1))
    x.append(5/0)
    x.append(int(3))
    print "This isn't printed if a ValueError is thrown"
except ValueError:
    print
    print sys.exc_info()[1]
except ArithmeticError:
    print
    print sys.exc_info()[1]
else:
    print "2. No exceptions were thrown and hence the else executed. If the commented divide by zero is uncommented, an exception will be thrown \and the else won't run"
