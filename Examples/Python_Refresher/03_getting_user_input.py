# name = input("Enter your name: ")
# print(name)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f'The size in square feet is {square_feet}. The size in square meters is {square_meters:.2f}')