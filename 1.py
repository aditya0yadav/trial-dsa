def func(integer):
    remainer = []
    while integer > 0:
        remainer.append(integer % 2)
        integer //= 2
    return remainer[::-1]

binary_digits = func(13)
print("Binary:", binary_digits)

# Convert binary list back to decimal for verification
total = 0
for bit in binary_digits:
    total = total * 2 + bit
print("Decimal:", total)
