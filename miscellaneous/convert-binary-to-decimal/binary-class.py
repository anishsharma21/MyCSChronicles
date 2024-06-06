class InvalidBinaryOperationException(Exception):
    pass

class Binary:
    def __init__(self, value='') -> None:
        if not isinstance(value, str):
            raise ValueError("Input value must be a string")
        self.value = value

    def to_dec(self):
        return sum([2**(len(self.value) - i - 1) if self.value[i] == '1' else 0 for i in range(len(self.value))])

    def add(self, num):
        if isinstance(num, Binary):
            if len(num.value) == len(self.value):
                return self._adder(self.value, num.value)
            else:
                raise InvalidBinaryOperationException(f"Original binary number not equal in length to new binary number. Length of {self.value} != length of {num.value}\n")
        else:
            raise InvalidBinaryOperationException("Input is not of type Binary")
    
    def _adder(self, b1, b2):
        final_b = ''
        carry = '0'
        for i in range(len(b1)-1, -1, -1):
            if carry == '0':
                if b1[i] == b2[i]:
                    carry = '1' if b1[i] == '1' else '0'
                    final_b = '0' + final_b
                else:
                    carry = '0'
                    final_b = '1' + final_b
            else:
                if b1[i] == b2[i]:
                    carry = '1' if b1[i] == '1' else '0'
                    final_b = '1' + final_b if b1[i] == '0' else '0' + final_b
                else:
                    carry = '1'
                    final_b = '0' + final_b
            if i == 0 and carry == '1':
                final_b = '1' + final_b
        return Binary(str(final_b))

b1 = Binary('10001011')
b2 = Binary('00101101')
b3 = None
try:    
    b3 = b1.add(b2)
    print(b1.to_dec())
    print(b2.to_dec())
    print(f"Binary Value: {b3.value}")
    print(f"Decimal Value: {b3.to_dec()}")
except InvalidBinaryOperationException as e:
    print('\nRan into an error: ' + e.args[0])