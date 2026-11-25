
from sortedcontainers import SortedList, SortedKeyList
sl = SortedList([30, 10, 40, 11, 50])
print(sl)
sl.add(23)
print(sl)

words = SortedKeyList(["kiwi", "banana", 
                       "grape", "fig"], key=lambda s:s[0])
print(words)
words.add("Fig")
print(words)