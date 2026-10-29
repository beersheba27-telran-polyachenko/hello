import random
nums = [] # emty list
i = 0
while i < 7:
    print("i =", i)
    i += 1

print("end of loop i =", i)

def is_exists(my_list, number):
    for x in my_list:
        if x == number:
            return True
    return False


ml = [0, 9, -3, -4, 4, 9, 6]
res = is_exists(ml, 3)
print(res)


nums = []
i = 0
while i < 7:
    n = random.randint(-5, 10)
    if is_exists(nums, n) == False:
        nums.append(n)
        print(nums)
    i += 1

print(nums)