#.   0. 1. 2
a = [1, 2, 3]
b = a
c = [1, 2, 3]
"""
b -> a -> [1, 2, 3]
c -> [1, 2, 3]

"""
print(a == c)
print(a == b)
print(a is b)
print(a is c)
a.append(4)
print(a)
print(b)
b.append(5)
print(a)

l1 = [1, 2, 3]
l1 = l1 + [5]
print(l1)
l1 += [6]
print(l1)

l1 = [1, 2, 3]
l2 = l1
"""
l2 -> l1 -> [1, 2, 3]
"""
l1 += [4]
print(l1 is l2)

l1 = [2, 3]
l2 = [2]
l3 = [l1, l2]
print(l3)
#           0     1
# l3 -> [[2, 3],[2, 5], [9]]
l2.append(5)
print(l3)
l3.append([9])
print(l3)

p1 = ["Ilan", 1234, 23]
p2 = ["Hanna", 6543, 21]
p3 = ["Alex", 4455, 27]

b1 = [p1, p2, p3]
print(b1)
p1[2] = 24
print(b1)

b2 = b1.copy()
print(b1 is b2)
print(p1 is b2[0])

from copy import deepcopy
b3 = deepcopy(b1)
print(b3)
print(b1 is b3)
print(p1 is b3[0])