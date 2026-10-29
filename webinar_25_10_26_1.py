# nums -> list
import random

nums = []
print(nums)
print(len(nums))
nums.append(9)
nums.append(12)
nums.append(7)
#          0   1  2
# nums -> [9, 12, 7]
print(nums)
print(nums[1])
nums[2] = -5
print(nums)

nums = [9, 2, -7, 23, 4, 18, -2]
#       x
for x in nums:
    print(x, end=" ")

print()

ages = [18, 37, 54, 26, 45, 19, 29]
#       x       
res = 0
for x in ages:
    res = res + x

quantity = len(ages)
average = res // quantity
print(average)


nums = []
# size = 9   |----------|
#            0          9  
#            i
for i in range(9):
    n = random.randint(-7, 10)
    nums.append(n)

print(nums)

for n in nums:
    if n % 2 == 0:
        print(n, end= ", ")