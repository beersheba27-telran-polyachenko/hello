import random
def exists(numbers, num):
    """
    returns True if "num" exists in list "numbers" otherwise False 
    """
    #TODO
    i = 0
    size = len(numbers)
    while i < size and numbers[i] != num:
        i += 1
    return i < size

def distinct_random_numbers(min, max, size):
    """
    
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """
    #TODO
    if (max - min + 1) < size:
        return []
    res = []
    while len(res) < size:
        num = random.randint(min, max)
        if not exists(res, num):
            res.append(num)
    return res

print (distinct_random_numbers(1, 49, 7))