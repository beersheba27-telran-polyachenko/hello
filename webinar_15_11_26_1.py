from webinar_15_11_26 import calculate
#.         "Hello"  "world"
def concat(s1: str, s2: str):
    return s1 + " " + s2

res = concat("hello", "world")
print(res)

res = calculate("money", "happy", concat)
print(res)

def do_any(a, func):
    result = func(a)
    print(result)

def div_3(a):
    return a / 3

def add_10(a):
    return a + 10

def multiply_100(a):
    return a * 100

do_any(30, multiply_100)
do_any(30, add_10)
do_any(30, div_3)