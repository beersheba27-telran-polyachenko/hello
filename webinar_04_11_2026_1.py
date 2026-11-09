def count(l: list[int], a: int):
   c = 0
   for n in l:
      if n == a:
         c += 1
   return c

print(count([10, 20, 30, 20, -1], 20))

l = [27, 3, 4, -11, 45]
def search_min(l: list[int]):
   m = l[0]
   for n in l:
      if n < m:
         m = n
   return m

print(search_min(l))