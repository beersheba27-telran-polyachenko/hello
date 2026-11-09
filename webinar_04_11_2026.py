a: float = 5.4
print(a)
a = "Hello"
print(a)
a = False
print(a)
my_list: list[float] = [5.1, 6.4, 8.2]
g : None = None

def do_any(c: int, d: str)-> int:
    print(d + str(c))
    return c + int(d)

s = do_any(23, "45")
print(s)