''' Note that if the list is not already sorted, you have to sort it yourself. Bisect will NOT do it. '''

import bisect

l1= [1,2,3,8]
el= 8

#Get list offset where you should insert an element
t1= bisect.bisect_left(l1, el)
print t1
t2= bisect.bisect_right(l1, el)
print t2

#Actually insert the element and automatically resort the list
bisect.insort_left(l1, el)
print l1
bisect.insort_right(l1, el)
print l1
