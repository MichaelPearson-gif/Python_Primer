# print((lambda x, y: x + y)(5, 7))

from typing import Sequence


# def double(x):
#     return x * 2

sequence = [1, 3, 5, 9]
doubled = [(lambda x: x * 2) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
