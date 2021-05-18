def mulitply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == "*":
        return mulitply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1, 3, 6, 7, operator="*"))
# print(mulitply(1, 3, 5))

# def add(x, y):
#     return x + y

# nums = {"x": 15, "y": 25}
# print(add(**nums))