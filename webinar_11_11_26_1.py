# 0
#O(1),  O(N),   O(N^2)

# O(1)
#.   0. 1. 2. 3.  4. 5
l = [8, 2, 7, 4, -3, 8]
print(l[3])

# O(N)
l = [8, 2, 7, 4, -3, 3]
#.   n
for n in l:
    if n == 4:
        print(n)

# O(N^2)
l = [8, 2, 7, 4, -3, 3]
i = 0
while i < len(l):
    j = len(l) - 1
    while j >= 0:
        if l[i] + l[j] == 10:
            print(i,j)
        j -= 1
    i += 1