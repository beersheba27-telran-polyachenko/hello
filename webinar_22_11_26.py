def subtract(num1: float, num2: float)->float:
    return num1 - num2

res = subtract(52.3, 3.2)
print(res)
res = subtract(num1= 12.2, num2= 6.5)
print(res)

def multiply( num1: float, *, num2: float):
    return num1 * num2

res = multiply(num2= 5, num1= 4)
print(res)
res = multiply(4, num2= 5)
print(res)

def add(num1: float, /, *, num2: float):
    return num1 + num2

res = add(6, num2= 8)
print(res)
res = add(8, num2= 6)
print(res)

def do_any(a, b, /, c, *, d, e):
    return a + b + c + d + e

res = do_any(2, 5, 4, d= 7, e= 6)
print(res)