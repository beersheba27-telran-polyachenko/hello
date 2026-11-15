student = [("Haim", 77), 
           ("Anna", 89), 
           ("Alex", 72),
           ("Max", 81)]
print(student)
student.sort()
print(student)
student.sort(key=lambda s: s[1])
print(student)

fruits = ["kiwi", "apple", "lemon", "bar"]
fruits.sort()
print(fruits)
fruits.sort(key=lambda w: len(w))
print(fruits)