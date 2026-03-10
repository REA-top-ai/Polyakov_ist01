single_digit = [x for x in range(10)]

squares = []

for item in single_digit:
    squares.append(item ** 2)
    print(item)

print(squares)

cubes = [item ** 3 for item in single_digit]
print(cubes)