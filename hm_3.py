def indexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
        indexOf([10, 20, 30, 20, -1],23) => -1
    """
    #TODO
    for i in range(len(numbers)):
        if numbers[i] == num:
            return i
    return -1

numbers = [0, 1, 2, 3, 4]
print(indexOf(numbers,5))