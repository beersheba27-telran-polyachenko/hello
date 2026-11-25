#        i
#        0   1   2   3   4   5   6   7   
#  l ->[23, 21, 45, 34, 52, 20, 61, 15]

from typing import Callable
def remove_predicate(l: list, 
                    predicate: Callable[[int], bool]):
    i = 0
    while i < len(l):
        if predicate(l[i]) == True:
            del l[i]
        else:
            i += 1

#          i
#          0   1  2  3   4  5  6 
my_list = [2, -3, 4, 5, -6, 7, 8]

remove_predicate(my_list, lambda x: x < 0)
print(my_list)

remove_predicate(my_list, lambda x: x % 2 != 0)
print(my_list)

def is_positive(number):
    if number > 0:
        return True
    else:
        return False

my_list = [2, -3, 4, 5, -6, 7, 8]
remove_predicate(my_list, is_positive)
print(my_list)