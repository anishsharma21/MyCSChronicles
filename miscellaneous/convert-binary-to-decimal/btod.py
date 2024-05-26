binary = input("Binary: ")
decimal = 0
for i in range(len(binary)):
    decimal += 2**i * int(binary[len(binary) - i - 1])
print(decimal)
#I should also implement a binary validator