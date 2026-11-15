from typing import Callable

def compute(a: float, b: float,
func: Callable[[float, float], float]):
    result: float = func(a, b)
    return result

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def add_10(a):
    return a + 10

res = compute(2.5, 3.6, subtract)
print(res)
res = compute(2.5, 3.6, add)
print(res)
res = compute(2.5, 3.6, multiply)
print(res)
res = compute(2.5, 3.6, add_10)
print(res)