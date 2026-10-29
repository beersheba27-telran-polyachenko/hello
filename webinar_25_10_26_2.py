import random
# tickets = [27, 34, 99, 15, 77, 49, 23]
# number = 15

def have_winner(tickets, number):
    for n in tickets:
        if n == number:
            return "you are winner !!!"
    return "next time..."

nums = []
for i in range(9):
    n = random.randint(1, 100)
    nums.append(n)

res = have_winner(nums, 13)
print(res)
print(have_winner(nums,75))