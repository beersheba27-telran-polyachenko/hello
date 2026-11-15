from typing import Callable
def add(a, b):
    return a + b

res = add(2, 5)
res = add(4, 1)
res = add(6, 12)

# addition = lambda a, b: a + b

def calculate(a, b, func: Callable[[float, float], float]):
    return func(a, b)

res = calculate(3, 7, lambda a, b: a + b)
print(res)
res = calculate(3, 7, lambda a, b: a - b)
print(res)
res = calculate(3, 7, lambda a, b: a * b)
print(res)

res = calculate(13, 7, 
                lambda a, b:
                a if a > b else b)
print(res)

res = calculate(2, 3,
                lambda a, b:
                a ** b)
print(res)

res = calculate(10, 3,
                lambda a, b:
                a % b)
print(res)

res = calculate(10, 3,
                lambda a, b:
                a // b)
print(res)