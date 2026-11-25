
from typing import Sequence, Callable, cast

def do_any(func: Callable[[int], int], value):
    res = func(value)
    print(res)

def add_10(x: int)->int:
    return x + 10

do_any(add_10, 23)

# Sequence
# [9, 2, 4, 7]
# (6.2, 23.3, 1.12, 17.5)
# "abcd"

def add_to_sequence(seq:
         Sequence[int|float|str], item):
    # seq = cast(list, seq)
    seq = list(seq)
    seq.append(item)
    
    return seq

int_list = [9, 2, 4, 7]
res = add_to_sequence(int_list, 8)
print(res)

float_tuple = (6.2, 23.3, 1.12, 17.5)
res = add_to_sequence(float_tuple, 4.7)
print(res)

s = "abc"
res = add_to_sequence(s, "d")
print(res)
