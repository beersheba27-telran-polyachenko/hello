def add(a, b):
    return a + b

def div(a, b):
    return a / b

f = add
print(type(f))
res = f(5, 6)
print(res)
f = div
res = f(5, 6)
print(res)

def percent(a, b):
    return(a * b) / 100


def calculate(a: float, b: float, fun):
    return fun(a, b)

print(calculate(80, 20, percent))