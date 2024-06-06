class InvalidBinaryOperationException(Exception):
    pass

class Binary:
    def __init__(self, value='') -> None:
        if not isinstance(value, str):
            raise ValueError("Input value must be a string")
        self.value = value

    def add(self, num):
        if isinstance(num, Binary):
            if len(num.value) == len(self.value):
                return self._adder(self.value, num.value)
            else:
                raise InvalidBinaryOperationException(f"Original binary number not equal in length to new binary number. Length of {self.value} != length of {num.value}\n")
        else:
            raise InvalidBinaryOperationException("Input is not of type Binary")
    
    def _adder(self, b1, b2): # not done
        final_b = ''
        carry = '0'
        for i in range(len(b1), 0, -1):
            c = '0' if b1[i-1] == b2[i-1] else '1'
            if b1[i-1] == '1' and c == '0':
                carry = '1'
            final_b = str(c) + str(final_b)
            if i-1 == 0 and c == '0' and b1[i-1] == '1':
                final_b = str(c) + str(final_b)
        return final_b

b1 = Binary('011')
b2 = Binary('101')
try:    
    print(b1.add(b2))
except InvalidBinaryOperationException as e:
    print('\nRan into an error: ' + e.args[0])