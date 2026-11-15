#.   0. 1   2. 3. 4. 5. 6
l = [7, 2, -3, 4, 5, 6, 1]
# l.sort()
# l -> [7, 2, -3, 4, 5, 6, 1] l.sort()
# l -> [-3, 1, 2, 4, 5, 6, 7]
# print(l)

my_list = sorted(l)
# l -> [7, 2, -3, 4, 5, 6, 1] sorted(l)
# l -> [7, 2, -3, 4, 5, 6, 1]
# my_list -> l [[-3, 1, 2, 4, 5, 6, 7]
#print(l)
#print(my_list)

my_list = sorted(l[1:5])
#print(my_list)

# bubble sort
#         0  1.  2. 3. 4. 5. 6
#   l -> [2, -3, 4, 7, 6, 1, 5] len(l) = 7

def max_to_end(numbers: list):
    i = 0
    flag = True
    while i < len(numbers) - 1:
        if numbers[i] > numbers[i+1]:
            temp = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = temp
            flag = False
        i += 1
    return flag

def bubble_sort(numbers: list):
    res = False
    while res == False:
        res = max_to_end(numbers)
    

l = [2, -3, 4, 7, 6, 1, 5]
bubble_sort(l)
print(l)