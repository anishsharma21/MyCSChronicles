from typing import Literal

BinaryType = Literal['unsigned', 'signed', 'twos-complement']

class InvalidBinaryOperationException(Exception):
    pass

class Binary:
    def __init__(self, value='0', type: BinaryType='unsigned') -> None:
        if type not in ['unsigned', 'signed', 'twos-complement']:
            raise ValueError("Invalid type. Type must be one of 'unsigned', 'signed', 'twos-complement'")
        if not isinstance(value, str):
            raise ValueError("Input value must be a string")
        
        self.value = value
        self.type = type

    def to_dec(self):
        if self.type == 'unsigned':
            return sum([2**(len(self.value) - i - 1) if self.value[i] == '1' else 0 for i in range(len(self.value))])
        elif self.type == 'signed':
            base_dec = sum([2**(len(self.value) - i - 1) if self.value[i] == '1' else 0 for i in range(1, len(self.value))])
            return -base_dec if self.value[0] == '1' else base_dec
        elif self.type == 'twos-complement':
            rev_bin = Binary(''.join(['1' if self.value[i] == '0' else '0' for i in range(len(self.value))]))
            rev_bin_add = rev_bin.add(Binary(''.join(['1' if i == len(self.value) - 1 else '0' for i in range(len(self.value))])))
            if rev_bin_add.value[0] == '0' and self.value[0] == '1':
                rev_bin_add.value = '1' + rev_bin_add.value
            base_dec = sum([2**(len(rev_bin_add.value) - i - 1) if rev_bin_add.value[i] == '1' else 0 for i in range(len(rev_bin_add.value))])
            return -base_dec if self.value[0] == '1' else base_dec
            

    def add(self, num): # needs to check that types are the same or needs to convert types / choose a type
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

b1 = Binary('1011', type='unsigned')
b2 = Binary('0101')
print(b1.add(b2).value)
print(b1.add(b2).to_dec())
b3 = Binary('11011', type='signed')
print(b3.to_dec())
b4 = Binary('1110101', type='twos-complement')
print(b4.to_dec())
