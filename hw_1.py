def print_predicate(l: list,
                    predicate):
# use for loop
    res = []
    for x in l:
        if predicate(x) == True:
            res.append(x)
    return res

int_list = [9, -2, 8, -6, 3, -5, 6]

# the function should print:
# even
res = print_predicate(int_list, lambda x: x % 2 == 0)
# [-2, 8, -6, 6]
print(res)

# the function should print:
# odd
res = print_predicate(int_list, lambda x: x % 2 != 0)
# [9, 3, -5]
print(res)

# the function should print:
# positive
def positive(x: int)->bool:
    if x < 0:
        return False
    else:
        return True

res = print_predicate(int_list, positive)
# [9, 8, 3, 6]
print(res)

# the function should print:
# negative
def negative(x: int)->bool:
    if x >= 0:
        return False
    else:
        return True
res = print_predicate(int_list, negative)
# [-2, -6, -5]
print(res)