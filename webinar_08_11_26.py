# ==, is, is not   True / False
#    0  1  2   3
#   [7, 2, 8, -2]
a: list = [1, 2, 3]
b: list = [1, 2, 3]
c = a
print("a == b ?", a == b) #True
print("a is b ?", a is b) #False
print("a is not b ?", a is not b) #True
print("c is a ?", c is a) #True

"""
a => [1, 2, 3]
b => [1, 2, 3]
c => a => [1, 2, 3]

"""