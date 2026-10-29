nums = []
for x in range(5,15):
    nums.append(x)

print(nums)
nums.clear()
# list generator
nums = [x for x in range(5, 15)]
print(nums)