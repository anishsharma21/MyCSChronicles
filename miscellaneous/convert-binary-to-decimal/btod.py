def validate_binary(binary):
    return all(char in ['0', '1'] for char in binary)

while True:
    binary = input("Binary: ")
    if binary == 'c':
        break
    decimal = 0
    if validate_binary(binary):
        for i in range(len(binary)):
            decimal += 2**i * int(binary[len(binary) - i - 1])
        print(decimal)
    else:
        print("Not valid binary")