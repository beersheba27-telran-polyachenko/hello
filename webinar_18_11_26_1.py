from bisect import *
#.   0. 1. 2.  3.  4
l = [4, 7, 9, 12, 27]
print(l)
i = bisect_left(l, 11)
print(i)
i = bisect_right(l, 11)
print(i)
print(l)
l.insert(i, 11)
print(l)
