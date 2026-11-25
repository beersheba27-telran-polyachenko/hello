from bisect import *
#.   0. 1. 2.  3.  4
l = [4, 7, 9, 10, 12, 27]
print(l)
i = bisect_left(l, 10)
print(i)
i = bisect_right(l, 10)
print(i)
insort(l, 20)
print(l)