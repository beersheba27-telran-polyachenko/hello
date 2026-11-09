def max_with_negative_duplicate (numbers:list[int]) -> int:
    """
    Algorithm complexity should be O[N]
    numbers - list with integer numbers
    returns the maximal element of "numbers" with existing negative duplicate 
    (example of a number with negative duplicate: number 100, negative duplicate -100)
    If no such number exists, returns -1
    Examples: max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) => 100
    max_with_negative_duplicate([10, 20, -15, -11, 20]) => -1
    """

    numbers_set: set = set(numbers)
    max_value: int = 0
    for num in numbers_set:
        if num > max_value:
            if - num in numbers_set:
                max_value = num
    return max_value

list_1: list[int] = [-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]
print(max_with_negative_duplicate(list_1))